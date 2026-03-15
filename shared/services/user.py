from sqlalchemy.ext.asyncio import AsyncSession

from shared.repositories.user import UserRepository


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_or_create(self, tg_user):
        user = await self.get_user(tg_user.id)
        if not user:
            user = await UserRepository(self.session).create(tg_user.id, tg_user.first_name,
                                                tg_user.last_name, tg_user.username)
            await self.session.commit()
        return user


    async def get_user(self, user_id):
        user = await UserRepository(self.session).get_by_id(user_id)
        if user:
            return user
