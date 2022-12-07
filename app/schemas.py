from pydantic import BaseModel


class Departament(BaseModel):
    depname: str
    zonesv_id: int
    isocode: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {"depname": "San Salvador", "zonesv_id": 2, "isocode": "SV-SS"}
        }


class Township(BaseModel):
    munname: str
    depsv_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {"munname": "Colon", "devps_id": 3}
        }


class Zone(BaseModel):
    zonename: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {"zonename": "Occidental"}
        }
