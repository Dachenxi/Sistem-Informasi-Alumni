from .prodi import Major
from .fakultas import Faculty

class Alumni:
    def __init__(self, nim: str, name: str, grad_year: int, entry_year: int, email: str, phone_number: str, major_id: int, major: Major, faculty: Faculty):
        self.nim = nim
        self.name = name
        self.graduation_year = grad_year
        self.entry_year = entry_year
        self.email = email
        self.phone_number = phone_number
        self.major_id = major_id
        self.major = major # Stores a full Major object
        self.faculty = faculty # Stores a full Faculty object

    @staticmethod
    def from_dict(data: dict, majors_map: dict):
        """
        Assembles an Alumni object from a DB row and a map of Major objects.
        :param data: A dictionary from the 'alumni' table row.
        :param majors_map: A dict mapping major_id → Major object.
        """
        major_id = data.get("id_prodi")
        major_object = majors_map.get(major_id)
        faculty_id = data.get("id_fakultas")
        faculty_object = majors_map.get(faculty_id)

        return Alumni(
            nim=data.get("nim", ""),
            name=data.get("nama", ""),
            grad_year=data.get("tahun_lulus", 0),
            entry_year=data.get("angkatan", 0),
            email=data.get("email", ""),
            phone_number=data.get("nomor_telepon", ""),
            major_id=data.get("id_prodi", 0),
            major=major_object, # Pass the found Major object
            faculty=faculty_object # Pass the found Faculty object
        )