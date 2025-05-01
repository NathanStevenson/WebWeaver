from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update, Column, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    # default constructor (email, password)
    def __init__(self, email, hashed_password):
        self.email = email
        self.hashed_password = hashed_password
    
    # mapped column is preferred over column in modern sql alchemy due to typing
    # mapped column you declare the type inside Mapped[] and it works better for type checking; cleaner code; designed for modern sql alchemy as compared to classic Column()

    user_name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column() 
    # profile_image; posts; messages; items; payment method; misc items -- all should be optional (this will need to be rendered by jinja with fields based on config given)
    
    # gets the user by their unique email; will return first found (email is unique) or None - never throws an Exception
    @classmethod
    async def get_user_by_email(cls, session: AsyncSession, email: str):
        return await session.execute(select(cls).filter_by(email=email)).scalars().first()