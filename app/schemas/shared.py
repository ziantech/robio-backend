from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class AddressObject(BaseModel):
    city: Optional[str]
    county: Optional[str]
    street: Optional[str]
    region: Optional[str]
    country: str = "România"


class DateObject(BaseModel):
    day: Optional[int]
    month: Optional[int]
    year: int
    circa: bool = False


class ChangeRecord(BaseModel):
    field: str  # Which field was changed (e.g. "first", "sex", "birth.place.city")
    from_: str  # Previous value (stored as string for consistency)
    to: str  # New value
    changed_at: datetime  # When the change occurred
    reason: Optional[str] = None  # Optional explanation for the change
    sources: List[str] = []


