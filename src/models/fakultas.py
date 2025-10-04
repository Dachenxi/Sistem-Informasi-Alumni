class Faculty:
    def __init__(self, id: int, name: str, code: str = ""):
        self.id = id
        self.name = name
        self.code = code

    @staticmethod
    def from_dict(data: dict):
        return Faculty(
            id=data.get("id_fakultas"),
            name=data.get("nama_fakultas", ""),
            code=data.get("kode_fakultas", "")
        )