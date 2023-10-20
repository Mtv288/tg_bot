from aiogram import F, Router
from aiogram.types import Message
from bot.keyboard import reply_keyboard


router = Router()


@router.message(F.text == 'Мужская обувь')
async def men(message: Message):
    await message.answer('Выберите категорию', reply_markup=reply_keyboard.men_kb)
