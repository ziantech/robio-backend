
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class SourceObject(BaseModel):
    id: str
    title: str
    volume: Optional[str] = None
    page: Optional[str] = None
    year: Optional[int] = None
    files: List[str] = []
    uploaded_by: str
    created_at: datetime