from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shared.db.models import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def create(self, id, first_name, last_name, username):
        user = User(id=id, first_name=first_name, last_name=last_name, username=username)
        self.session.add(user)
        return user


    async def get_by_id(self, id: int):
        result = await self.session.execute(
            select(User).where(User.id == id)
        )
        return result.scalar_one_or_none() 
