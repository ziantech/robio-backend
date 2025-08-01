from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from datetime import datetime


# ✅ Track changes to name fields (with sources)
class NameChange(BaseModel):
    field: str
    from_: str
    to: str
    changed_at: datetime
    reason: Optional[str] = None
    sources: List[str] = [] 


# ✅ Complete name structure
class NameObject(BaseModel):
    title: Optional[str]
    first: List[str]
    last: str
    maiden: Optional[str]
    suffix: Optional[str]
    reason: Optional[str]
    changes: List[NameChange] = []
    sources: List[str] = []


# ✅ Biological sex enum
class SexEnum(str, Enum):
    male = "male"
    female = "female"
    unknown = "unknown"


# ✅ Track changes to sex (with sources)
class SexChange(BaseModel):
    from_: SexEnum
    to: SexEnum
    changed_at: datetime
    reason: Optional[str] = None
    sources: List[str] = []


# ✅ Complete sex structure with history and verification
class SexObject(BaseModel):
    value: SexEnum
    reason: Optional[str]
    sources: List[str] = []
    changes: List[SexChange] = []
