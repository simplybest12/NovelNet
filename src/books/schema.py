from pydantic import BaseModel
from datetime import datetime,date

class Book(BaseModel):
    id:int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime
    
class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str   
     
class BookResponse(BookCreate):
    
    class Config:
        from_attributes = True