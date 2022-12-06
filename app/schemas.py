from pydantic import BaseModel


class Departament(BaseModel):
    depname: str
    zonesv_id: int
    isocode: str

    class Config:
        orm_mode = True


class Township(BaseModel):
    name: str
    departament_id: int

    class Config:
        orm_mode = True
