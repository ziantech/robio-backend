from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.location import Commune, County, Region, Settlement
from app.schemas.geo import RegionOut, CountyOut, CommuneOut, SettlementOut

router = APIRouter()


@router.get("/regions", response_model=List[RegionOut])
def get_regions(db: Session = Depends(get_db)):
    return db.query(Region).all()


@router.get("/counties", response_model=List[CountyOut])
def get_counties(db: Session = Depends(get_db)):
    results = (
        db.query(County, Region.name.label("region_name"))
        .join(Region)
        .all()
    )
    return [
        CountyOut(
            id=c.id,
            name=c.name,
            status=c.status,
            modern_name=c.modern_name,
            region_id=c.region_id,
            region_name=region_name,
        )
        for c, region_name in results
    ]


@router.get("/communes", response_model=List[CommuneOut])
def get_communes(db: Session = Depends(get_db)):
    results = (
        db.query(Commune, County.name.label("county_name"))
        .join(County)
        .all()
    )
    return [
        CommuneOut(
            id=c.id,
            name=c.name,
            status=c.status,
            modern_name=c.modern_name,
            county_id=c.county_id,
            county_name=county_name,
        )
        for c, county_name in results
    ]


@router.get("/settlements", response_model=List[SettlementOut])
def get_settlements(db: Session = Depends(get_db)):
    results = (
        db.query(Settlement, Commune.name.label("commune_name"))
        .outerjoin(Commune)
        .all()
    )
    return [
        SettlementOut(
            id=s.id,
            name=s.name,
            type=s.type,
            status=s.status,
            modern_name=s.modern_name,
            county_id=s.county_id,
            commune_id=s.commune_id,
            commune_name=commune_name,
        )
        for s, commune_name in results
    ]
