from typing import Optional

from pydantic import BaseModel


class Departament(BaseModel):
    departament_name: str
    zone_id: int
    zone: Optional[str] = None


class Township(BaseModel):
    township_name: str
    departament_id: int
    departament: Optional[str] = None
