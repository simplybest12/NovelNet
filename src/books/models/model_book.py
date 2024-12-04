from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, Date
from sqlalchemy.orm import relationship
from datetime import datetime
import random
from ...db.database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    published_date = Column(Date, nullable=False)
    page_count = Column(Integer, nullable=False)
    language = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())  