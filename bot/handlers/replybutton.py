from aiogram import F, Router
from aiogram.types import Message
from bot.keyboard import reply_keyboard
from aiogram.filters import Command, CommandStart


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет')
    await message.answer('Выберите категорию', reply_markup=reply_keyboard.main_kb)

