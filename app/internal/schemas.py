from pydantic import BaseModel


class Department(BaseModel):
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


class Zipzip(BaseModel):
    depname: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "Antiguo Cuscatlán": "01502",
                "Chiltiupán": "01507",
                "Ciudad Arce": "01504",
                "Colón": "01512",
                "Comasagua": "01506",
                "Huizúcar": "01508",
                "Jayaque": "01509",
                "Jicalapa": "01510",
                "La Libertad": "01511",
                "Santa Tecla\nAntes: Nueva San Salvador": "01501",
                "Nuevo Cuscatlán": "01513",
                "San Juan Opico": "01514",
                "Quezaltepeque": "01515",
                "Sacacoyo": "01516",
                "San José Villanueva": "01517",
                "San Matías": "01518",
                "San Pablo Tacachico": "01519",
                "Talnique": "01521",
                "Tamanique": "01522",
                "Teotepeque": "01523",
                "Tepecoyo": "01524",
                "Zaragoza": "01525",
                "Summary": "San Salvador es un departamento fundado en 1865 ubicado en la Zona Central de El Salvador. Posee 3 distritos y 22 municipios.",
            }
        }
