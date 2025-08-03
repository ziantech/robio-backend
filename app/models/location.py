import uuid
from sqlalchemy import Column, String, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum


class GeoStatus(str, enum.Enum):
    active = "active"
    historical = "historical"


class Region(Base):
    __tablename__ = "regions"
    __table_args__ = {"schema": "robio"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), unique=True, nullable=False)
    status = Column(Enum(GeoStatus), default=GeoStatus.active)

    counties = relationship("County", back_populates="region", lazy="selectin")


class County(Base):
    __tablename__ = "counties"
    __table_args__ = {"schema": "robio"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    region_id = Column(UUID(as_uuid=True), ForeignKey("robio.regions.id"), nullable=True)
    status = Column(Enum(GeoStatus), default=GeoStatus.active)

    region = relationship("Region", back_populates="counties")
    communes = relationship("Commune", back_populates="county", lazy="selectin")
    settlements = relationship("Settlement", back_populates="county", lazy="selectin")


class Commune(Base):
    __tablename__ = "communes"
    __table_args__ = {"schema": "robio"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    county_id = Column(UUID(as_uuid=True), ForeignKey("robio.counties.id"), nullable=False)
    status = Column(Enum(GeoStatus), default=GeoStatus.active)

    county = relationship("County", back_populates="communes")
    settlements = relationship("Settlement", back_populates="commune", lazy="selectin")


class SettlementType(str, enum.Enum):
    city = "city"
    village = "village"


class Settlement(Base):
    __tablename__ = "settlements"
    __table_args__ = {"schema": "robio"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    type = Column(Enum(SettlementType), nullable=False)
    county_id = Column(UUID(as_uuid=True), ForeignKey("robio.counties.id"), nullable=False)
    commune_id = Column(UUID(as_uuid=True), ForeignKey("robio.communes.id"), nullable=True)
    status = Column(Enum(GeoStatus), default=GeoStatus.active)

    county = relationship("County", back_populates="settlements")
    commune = relationship("Commune", back_populates="settlements")
