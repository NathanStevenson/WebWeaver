from base_model import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update, Column, DateTime
from sqlalchemy.orm import Mapped, mapped_column

class User(BaseModel):
    __tablename__ = "users"

    # mapped column is preferred over column in modern sql alchemy due to typing
    # mapped column you declare the type inside Mapped[] and it works better for type checking; cleaner code; designed for modern sql alchemy as compared to classic Column()

    user_name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password