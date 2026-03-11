from sqlalchemy import BigInteger
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from shared.db.base import Base


class User(Base):
    '''таблица юзера'''

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(default="user")
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    phone: Mapped[str | None]
