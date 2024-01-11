from aiogram import F, Router
from aiogram.types import Message
import re


router = Router()


@router.message(lambda message: 'жен' in message.text.lower())
async def hello(message: Message):
    await message.reply(f'Найдено совпадение: ура')

