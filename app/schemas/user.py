from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.schemas.profile import NameObject, SexObject


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: str  # will be used in future auth
    profile: Optional["ProfileCreate"]  # nested profile (optional)


class UserOut(UserBase):
    id: UUID
    email_verified: bool
    is_banned: bool
    banned_until: Optional[datetime]
    earned_money: float
    subscription_active: bool
    subscription_expires_at: Optional[datetime]
    current_address: Optional[str]
    profile_id: Optional[UUID]

    class Config:
        orm_mode = True


class ProfileCreate(BaseModel):
    tree_ref: str
    name: NameObject
    sex: SexObject


UserCreate.update_forward_refs()
