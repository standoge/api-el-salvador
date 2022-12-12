from pydantic import BaseModel


class Departament(BaseModel):
    depname: str
    zonesv_id: int
    isocode: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "depname": "San Salvador",
                "isocode": "SV-SS",
                "id": 6,
                "zonesv_id": 2,
                "zone": {"zonename": "Central", "id": 2},
                "muns": [{"depsv_id": 6, "id": 200, "munname": "Aguilares"}, {"..."}],
            }
        }


class Municipality(BaseModel):
    munname: str
    depsv_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "depsv_id": 4,
                "id": 132,
                "munname": "Colón",
                "departament": {
                    "isocode": "SV-LI",
                    "depname": "La Libertad",
                    "id": 4,
                    "zonesv_id": 2,
                    "zone": {"zonename": "Central", "id": 2},
                },
            }
        }


class Zone(BaseModel):
    zonename: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "zonename": "Occidental",
                "departaments": [
                    {
                        "isocode": "SV-AH",
                        "depname": "Ahuachapán",
                        "id": 1,
                        "zonesv_id": 1,
                        "muns": [
                            {"munname": "Ahuachapán", "id": 1, "depsv_id": 1},
                            {"..."},
                        ],
                    },
                ],
            }
        }
