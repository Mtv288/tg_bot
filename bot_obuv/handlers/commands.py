from aiogram import Router
from aiogram.types import Message
from bot_obuv.keyboard.reply_keyboard import main_kb
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}')
    await message.answer('Я ваш виртуальный помощник', reply_markup=main_kb())
