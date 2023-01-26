from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.internal.db import Base


class Department(Base):
    __tablename__ = "depsv"

    id = Column(Integer, primary_key=True, index=True)
    depname = Column(String)
    isocode = Column(String)
    zonesv_id = Column(Integer, ForeignKey("zonesv.id"))
    muns = relationship("Municipality", lazy="joined", back_populates="department")
    zone = relationship("Zone", lazy="joined", back_populates="departments")

    def __repr__(self):
        return f"{self.__tablename__} - {self.depname}"


class Municipality(Base):
    __tablename__ = "munsv"

    id = Column(Integer, primary_key=True, index=True)
    munname = Column(String)
    depsv_id = Column(Integer, ForeignKey("depsv.id"), nullable=False)
    department = relationship("Department", lazy="joined", back_populates="muns")

    def __repr__(self):
        return f"{self.__tablename__} - {self.munname}"


class Zone(Base):
    __tablename__ = "zonesv"

    id = Column(Integer, primary_key=True, index=True)
    zonename = Column(String)
    departments = relationship("Department", lazy="joined", back_populates="zone")

    def __repr__(self):
        return f"{self.__tablename__} - {self.zonename}"
