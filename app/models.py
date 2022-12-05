from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Departament(Base):
    __tablename__ = "depsv"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, not_null=True)
    iso = Column(String, not_null=True)
    zone_id = Column(Integer, ForeignKey("zonesv.id"))

    zones = relationship("Zone", back_populates="departament")


class Zone(Base):
    __tablename__ = "zonesv"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, not_null=True)

    departaments = relationship("Departament", back_populates="zone")
