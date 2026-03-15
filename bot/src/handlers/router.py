from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters.command import Command

from shared.services.user import UserService
from src.utils import get_profile


root = Router()


@root.message(Command("start"))
async def start(message: Message, session) -> None:
    await UserService(session).get_or_create(message.from_user)
    await message.answer(text="start")


@root.message(Command("profile"))
async def show_profile(message: Message, session) -> None:
    user = await UserService(session).get_user(message.from_user.id)
    profile = get_profile(user)
    await message.answer(text=profile, parse_mode=ParseMode.MARKDOWN_V2)
