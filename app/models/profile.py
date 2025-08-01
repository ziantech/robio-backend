import uuid
from sqlalchemy import Column, DateTime, String, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.sql import func

class Profile(Base):
    __tablename__ = "profiles"
    __table_args__ = {"schema": "robio"}
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tree_ref = Column(String(20), unique=True, nullable=False)

    name = Column(JSON, nullable=False)  # Defined via Pydantic
    sex = Column(JSON, nullable=False)   # Defined via Pydantic
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    owner = relationship("User", back_populates="profile", uselist=False)
