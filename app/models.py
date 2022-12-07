from sqlalchemy import Column, ForeignKey, Integer, String

from db import Base


class Departament(Base):
    __tablename__ = "depsv"

    id = Column(Integer, primary_key=True, index=True)
    depname = Column(String)
    isocode = Column(String)
    zonesv_id = Column(Integer, ForeignKey("zonesv.id"))


class Township(Base):
    __tablename__ = "munsv"

    id = Column(Integer, primary_key=True, index=True)
    munname = Column(String)
    depsv_id = Column(Integer, ForeignKey("depsv.id"))


class Zone(Base):
    __tablename__ = "zonesv"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
