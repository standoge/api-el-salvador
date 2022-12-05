from typing import Optional

from pydantic import BaseModel


class Departament(BaseModel):
    departament_name: str
    zone_id: int

    class Config:
        orm_mode = True


class Township(BaseModel):
    township_name: str
    departament_id: int

    class Config:
        orm_mode = True
