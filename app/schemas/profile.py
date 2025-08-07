from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from datetime import datetime
from shared import AddressObject, ChangeRecord, DateObject


# ✅ Complete name structure
class NameObject(BaseModel):
    title: Optional[str]
    first: List[str] = []
 
    alternative: List[str] = []
    last: str
    maiden: Optional[str]
    suffix: Optional[str]
    changes: List[ChangeRecord] = []
    sources: List[str] = []


# ✅ Biological sex enum
class SexEnum(str, Enum):
    male = "male"
    female = "female"
    unknown = "unknown"


# ✅ Complete sex structure with history and verification
class SexObject(BaseModel):
    value: SexEnum
    sources: List[str] = []
    changes: List[ChangeRecord] = []


class BirthObject(BaseModel):
    date: Optional[DateObject] = None
    place: Optional[AddressObject] = None
    sources: List[str] = []  
    changes: List[ChangeRecord] = []

class DeathObject(BaseModel):
    date: Optional[DateObject] = None
    place: Optional[AddressObject] = None
    sources: List[str] = []  
    changes: List[ChangeRecord] = []