from aiogram import F, Router
from aiogram.types import Message
from bot.keyboard import reply_keyboard


router = Router()


@router.message(F.text == 'Назад')
async def back(message: Message):
    await message.answer('Главное меню', reply_markup=reply_keyboard.main_kb)


@router.message(F.text == 'Мужская обувь')
async def men(message: Message):
    await message.answer('Выберите категорию', reply_markup=reply_keyboard.men_kb)


@router.message(F.text == 'Женская обувь')
async def women(message: Message):
    await message.answer('Выберите категорию', reply_markup=reply_keyboard.women_kb)
