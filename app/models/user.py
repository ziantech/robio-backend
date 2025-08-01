import uuid
from sqlalchemy import Column, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.sql import func

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

    current_address = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    profile_id = Column(UUID(as_uuid=True), ForeignKey("robio.profiles.id"))
    profile = relationship("Profile", back_populates="owner", uselist=False)
