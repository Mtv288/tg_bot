from aiogram import F, Router
from aiogram.types import Message


router = Router()


@router.message(F.text == 'Привет')
async def hello(message: Message):
    await message.answer('Пока')

