from aiogram import F, Router
from aiogram.types import Message
from bot.keyboard import reply_keyboard
from aiogram.filters import Command, CommandStart

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}')
    await message.answer('Я ваш виртуальный помощник', reply_markup=reply_keyboard.main_kb)