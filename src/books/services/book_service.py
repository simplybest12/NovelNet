from sqlalchemy.orm import Session
from fastapi import HTTPException,Depends,status
from typing import Annotated
from ...db import database
from ..schema import BookCreate 
from ..models import model_book



get_db = database.get_db
db_dependency = Annotated[Session,Depends(get_db)]
class BookService:
    async def create_book(self, db: db_dependency, book_instance: BookCreate):
        db_book = model_book.Book(**book_instance.dict())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    
    async def get_all_books(self, db: db_dependency):
        books = db.query(model_book.Book).all().order_by(model_book.Book.created_at.desc())
        return books
    
    
    
    
    
    async def get_book_by_id(self, db: db_dependency, book_id: int):
        book = db.query(model_book.Book).filter(model_book.Book.id == book_id).first()
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {book_id} not found")
        return book
    