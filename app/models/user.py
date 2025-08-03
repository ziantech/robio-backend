import uuid
from sqlalchemy import Column, String, Boolean, DateTime, Float, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.sql import func
from enum import Enum
from sqlalchemy import Column, String, Enum as SQLEnum


class UserRole(str, Enum):
    user = "user"
    moderator = "moderator"
    admin = "admin"


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "robio"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    email_verified = Column(Boolean, default=False)

    is_banned = Column(Boolean, default=False)
    banned_until = Column(DateTime, nullable=True)

    earned_money = Column(Float, default=0.0)
    subscription_active = Column(Boolean, default=False)
    subscription_expires_at = Column(DateTime, nullable=True)
    password = Column(Text, nullable=False)
    private = Column(Boolean, default=False)
    recovery_email = Column(String(255), nullable=True)
    recovery_phone = Column(String(20), nullable=True)
    terms_accepted = Column(Boolean, default=False)

    current_address = Column(String(500), nullable=True)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    role = Column(
        SQLEnum(UserRole, name="userrole"), nullable=False, default=UserRole.user
    )

    profile_id = Column(UUID(as_uuid=True), ForeignKey("robio.profiles.id"))
    profile = relationship("Profile", back_populates="owner", uselist=False)
    uploaded_sources = relationship("Source", back_populates="uploaded_by")

from app.models.profile import Profile
from app.models.source import Source