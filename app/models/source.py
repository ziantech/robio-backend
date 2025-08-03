# app/models/source.py

import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Source(Base):
    __tablename__ = "sources"
    __table_args__ = {"schema": "robio"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    volume = Column(String(50), nullable=True)
    page = Column(String(50), nullable=True)
    year = Column(Integer, nullable=True)
    files = Column(JSON, nullable=True)  # List of file URLs or S3 keys

    uploaded_by_id = Column(UUID(as_uuid=True), ForeignKey("robio.users.id"), nullable=False)
    uploaded_by = relationship("User", back_populates="uploaded_sources")

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
