from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

router = Router()


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать')
    await message.answer('Я ваш помощник по чату')
    await message.answer('Могу ответить не некоторые вопросы')
