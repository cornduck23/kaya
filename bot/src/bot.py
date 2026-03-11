import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from src.handlers.router import root
from src.middleware.session import SessionMiddleware
from shared.config import settings


async def start_bot():    
    '''start bot'''

    API_TOKEN = settings.BOT_TOKEN
    bot = Bot(token=API_TOKEN)

    storage = RedisStorage.from_url(settings.REDIS_URL)
    dp = Dispatcher(storage=storage)
    dp.update.middleware(SessionMiddleware())
    dp.include_router(root)

    await dp.start_polling(bot)
