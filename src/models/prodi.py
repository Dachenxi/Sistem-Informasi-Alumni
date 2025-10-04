class Major:
    def __init__(self, id: int, name: str, code: str, acreditation: str):
        self.id = id
        self.name = name
        self.code = code
        self.acreditation = acreditation

    @staticmethod
    def from_dict(data: dict):
        """
        Assembles a Major object from a DB row and a map of Faculty objects.
        :param data: A dictionary from the 'prodi' table row.
        """

        return Major(
            id=data.get("id_prodi"),
            name=data.get("nama_prodi", ""),
            code=data.get("kode_prodi", ""),
            acreditation=data.get("akreditasi", "")
        )