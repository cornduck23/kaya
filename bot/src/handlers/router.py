from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command


root = Router()


@root.message(Command("start"))
async def start(message: Message, state) -> None:
    await message.answer(text="start")
