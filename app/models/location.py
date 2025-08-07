import uuid
from sqlalchemy import Column, Float, String, ForeignKey, Enum
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
    modern_name = Column(String(100), nullable=True)
    created_by_id = Column(UUID(as_uuid=True), ForeignKey("robio.users.id"), nullable=True)
    created_by = relationship("User", back_populates="created_regions")  
    counties = relationship("County", back_populates="region", lazy="selectin")


class County(Base):
    __tablename__ = "counties"
    __table_args__ = {"schema": "robio"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    region_id = Column(UUID(as_uuid=True), ForeignKey("robio.regions.id"), nullable=True)
    status = Column(Enum(GeoStatus), default=GeoStatus.active)
    modern_name = Column(String(100), nullable=True)
    created_by_id = Column(UUID(as_uuid=True), ForeignKey("robio.users.id"), nullable=True)
    created_by = relationship("User", back_populates="created_counties")

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
    modern_name = Column(String(100), nullable=True)
    created_by_id = Column(UUID(as_uuid=True), ForeignKey("robio.users.id"), nullable=True)
    created_by = relationship("User", back_populates="created_communes")

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
    modern_name = Column(String(100), nullable=True)
    created_by_id = Column(UUID(as_uuid=True), ForeignKey("robio.users.id"), nullable=True)
    created_by = relationship("User", back_populates="created_settlements")

    county = relationship("County", back_populates="settlements")
    commune = relationship("Commune", back_populates="settlements")


class Cemetery(Base):
    __tablename__ = "cemeteries"
    __table_args__ = {"schema": "robio"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=True)
    address = Column(String(255), nullable=True)

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    settlement_id = Column(UUID(as_uuid=True), ForeignKey("robio.settlements.id"), nullable=True)
    created_by_id = Column(UUID(as_uuid=True), ForeignKey("robio.users.id"), nullable=True)
    status = Column(Enum(GeoStatus), default=GeoStatus.active)

    settlement = relationship("Settlement")
    created_by = relationship("User", back_populates="created_cemeteries")
