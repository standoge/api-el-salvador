from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Departament(Base):
    __tablename__ = "depsv"

    id = Column(Integer, primary_key=True, index=True)
    depname = Column(String)
    isocode = Column(String)
    zonesv_id = Column(Integer, ForeignKey("zonesv.id"))
    muns = relationship("Township", lazy="joined", back_populates="departament")
    zone = relationship("Zone", lazy="joined", back_populates="departaments")


class Township(Base):
    __tablename__ = "munsv"

    id = Column(Integer, primary_key=True, index=True)
    munname = Column(String)
    depsv_id = Column(Integer, ForeignKey("depsv.id"), nullable=False)
    departament = relationship("Departament", lazy="joined", back_populates="muns")


class Zone(Base):
    __tablename__ = "zonesv"

    id = Column(Integer, primary_key=True, index=True)
    zonename = Column(String)
    departaments = relationship("Departament", lazy="joined", back_populates="zone")
