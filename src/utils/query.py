from database.database import Database
from src.models.fakultas import Faculty
from src.models.prodi import Major
from src.models.alumni import Alumni
import pathlib

root_path = pathlib.Path(__file__).parent.parent.parent.absolute()

db = Database(db_path=str(root_path / "database" / "database.db"))

def get_all_faculty():
    data = db.fetch("SELECT id_fakultas, nama_fakultas FROM fakultas")
    return [Faculty.from_dict(data) for data in data]

def get_all_prodi(faculty: int):
    data = db.fetch("SELECT * FROM prodi where id_fakultas = ?", (faculty,))
    return [Major.from_dict(data) for data in data]

def load_alumni_data(data):
    faculties_cache = {}
    majors_cache = {}
    alumni_list = []

    if not data:
        return []

    # Iterate through each flat row from the database
    for row in data:
        faculty_id = row['id_fakultas']
        major_id = row['id_prodi']

        # 1. Assemble the Faculty object (or get from cache)
        if faculty_id not in faculties_cache:
            faculties_cache[faculty_id] = Faculty(id=faculty_id, name=row['nama_fakultas'])
        faculty_object = faculties_cache[faculty_id]

        # 2. Assemble the Major object (or get from cache)
        if major_id not in majors_cache:
            majors_cache[major_id] = Major(
                id=major_id,
                name=row['nama_prodi'],
                code=row['kode_prodi'],
                acreditation=row['akreditasi'],
            )
        major_object = majors_cache[major_id]

        # 3. Assemble the final Alumni object
        alumni_object = Alumni(
            nim=row['nim'],
            name=row['nama'],
            grad_year=row['tahun_lulus'],
            entry_year=row['angkatan'],
            email=row['email'],
            phone_number=row['nomor_telepon'],
            major_id=row['id_prodi'],
            major=major_object,  # Use the complete Major object
            faculty=faculty_object  # Use the complete Faculty object
        )
        alumni_list.append(alumni_object)

    return alumni_list

def get_all_alumni() -> list[Alumni]:
    all_data = db.fetch("""
                        SELECT
                            a.id_alumni,
                            a.nim,
                            a.nama,
                            a.tahun_lulus,
                            a.angkatan,
                            a.email,
                            a.nomor_telepon,
                            a.id_prodi,
                            p.id_fakultas,
                            p.nama_prodi,
                            p.kode_prodi,
                            p.akreditasi,
                            f.nama_fakultas
                        FROM
                            alumni a
                                INNER JOIN prodi p on p.id_prodi = a.id_prodi
                                INNER JOIN fakultas f on f.id_fakultas = p.id_fakultas;""")


    return load_alumni_data(all_data)

def get_alumni_by_nim(nim: str) -> Alumni | None:
    data = db.fetch("""
                        SELECT a.id_alumni,
                               a.nim,
                               a.nama,
                               a.tahun_lulus,
                               a.angkatan,
                               a.email,
                               a.nomor_telepon,
                               a.id_prodi,
                               p.id_fakultas,
                               p.nama_prodi,
                               p.kode_prodi,
                               p.akreditasi,
                               f.nama_fakultas
                        FROM alumni a
                                 INNER JOIN prodi p on p.id_prodi = a.id_prodi
                                 INNER JOIN fakultas f on f.id_fakultas = p.id_fakultas
                        WHERE a.nim = ?;""", (nim,), one=True)

    faculty_object = Faculty(id=data['id_fakultas'], name=data['nama_fakultas'])
    major_object = Major(id=data['id_prodi'], name=data['nama_prodi'], code=data['kode_prodi'], acreditation=data['akreditasi'])
    alumni_object = Alumni(nim=data["nim"],
                           name=data["nama"],
                           grad_year=data["tahun_lulus"],
                           entry_year=data["angkatan"],
                           email=data["email"],
                           phone_number=data["nomor_telepon"],
                           major_id=data["id_prodi"],
                           major=major_object,
                           faculty=faculty_object)
    return alumni_object if data else None

def get_last_nim(id_prodi: int, angkatan: int):
    data = db.fetch("SELECT nim FROM alumni WHERE id_prodi = ? AND angkatan = ? ORDER BY nim DESC LIMIT 1;", (id_prodi,angkatan))
    last_digit = data[0]['nim'][-3:] if data else None
    return int(last_digit) if last_digit else 0

def get_dashboard_data():
    total_alumni = db.fetch("SELECT COUNT(*) as total FROM alumni")[0]['total']
    total_faculty = db.fetch("SELECT COUNT(*) as total FROM fakultas")[0]['total']
    total_major = db.fetch("SELECT COUNT(*) as total FROM prodi")[0]['total']
    return {
        "total_alumni": total_alumni,
        "total_faculty": total_faculty,
        "total_major": total_major
    }

def add_alumni(nim: str,
               nama: str,
               tahun_lulus:int,
               email: str,
               nomor_telepon: int,
               angkatan: int,
               id_prodi: int) -> bool:
    db.execute("""
                INSERT INTO alumni (nim, nama, tahun_lulus, email, nomor_telepon, angkatan, id_prodi)
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """, (nim, nama, tahun_lulus, email, nomor_telepon, angkatan, id_prodi))
    return True

def add_faculty(nama_fakultas: str) -> bool:
    check_duplicate = db.fetch("SELECT * FROM fakultas WHERE nama_fakultas = ?", (nama_fakultas,))
    if check_duplicate:
        return False

    db.execute("""
                INSERT INTO fakultas (nama_fakultas)
                VALUES (?);
                """, (nama_fakultas,))
    return True

def add_major(nama_prodi: str, kode_prodi: str, akreditasi: str, fakultas: str) -> bool:
    get_faculty_id_by_name = db.fetch("SELECT id_fakultas FROM fakultas WHERE nama_fakultas = ?", (fakultas,), one=True)
    check_duplicate = db.fetch("SELECT * FROM prodi WHERE nama_prodi = ? and id_fakultas = ?", (nama_prodi, get_faculty_id_by_name["id_fakultas"]))

    if check_duplicate:
        return False

    db.execute("""
                INSERT INTO prodi (nama_prodi, kode_prodi, akreditasi, id_fakultas)
                VALUES (?, ?, ?, ?);
                """, (nama_prodi, kode_prodi, akreditasi, get_faculty_id_by_name["id_fakultas"]))
    return True

def filter_alumni(filter_column: str, filter_value: str):
    allowed_columns = {
        "Nim": "a.nim",
        "Nama": "a.nama",
        "Prodi": "p.nama_prodi",
        "Fakultas": "f.nama_fakultas",
    }
    if filter_column not in allowed_columns:
        print(f"Error: Filtering by '{filter_column}' is not allowed.")
        return None

    safe_column_name = allowed_columns[filter_column]
    query = f"""
                    SELECT a.id_alumni,
                           a.nim,
                           a.nama,
                           a.tahun_lulus,
                           a.angkatan,
                           a.email,
                           a.nomor_telepon,
                           a.id_prodi,
                           p.id_fakultas,
                           p.nama_prodi,
                           p.kode_prodi,
                           p.akreditasi,
                           f.nama_fakultas
                    FROM alumni a
                             INNER JOIN prodi p on p.id_prodi = a.id_prodi
                             INNER JOIN fakultas f on f.id_fakultas = p.id_fakultas
                    WHERE {safe_column_name} LIKE ?;"""
    params = (f"{filter_value}%",)
    data = db.fetch(query, params)
    return load_alumni_data(data)
