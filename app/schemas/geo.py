from pydantic import BaseModel
from uuid import UUID
from enum import Enum
from typing import Optional


class GeoStatus(str, Enum):
    active = "active"
    historical = "historical"


class RegionOut(BaseModel):
    id: UUID
    name: str
    status: GeoStatus
    modern_name: Optional[str]

    class Config:
        orm_mode = True


class CountyOut(BaseModel):
    id: UUID
    name: str
    status: GeoStatus
    modern_name: Optional[str]
    region_id: Optional[UUID]
    region_name: Optional[str]

    class Config:
        orm_mode = True


class CommuneOut(BaseModel):
    id: UUID
    name: str
    status: GeoStatus
    modern_name: Optional[str]
    county_id: UUID
    county_name: Optional[str]

    class Config:
        orm_mode = True


class SettlementOut(BaseModel):
    id: UUID
    name: str
    type: Optional[str]
    status: GeoStatus
    modern_name: Optional[str]
    county_id: UUID
    commune_id: Optional[UUID]
    commune_name: Optional[str]

    class Config:
        orm_mode = True
