from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import keyboar as kb


router = Router()


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать', reply_markup=kb.main)
    await message.answer('Я ваш помощник в чате')
    await message.answer('Если хотите ознакомится с нашим ассортиментом нажмите нужную кнопку внизу')


@router.message(F.text == 'Мужская обувь')
async def mens(message: Message):
    await message.answer('Выберите категорию', reply_markup=kb.mens)
