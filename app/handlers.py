from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import keyboar as kb

router = Router()


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать', reply_markup=kb.main)
    await message.answer('Я ваш помощник в чате')
    await message.answer('Если хотите ознакомится с нашим ассортиментом нажмите нужную кнопку внизу')


@router.message(F.text)
async def mens(message: Message):
    if message.text == 'Мужская обувь':
        await message.answer('Выберите тип обуви', reply_markup=kb.mens)
    elif message.text == 'Женская обувь':
        await message.answer('Выберите тип обуви', reply_markup=kb.women)
    elif message.text == 'Детская обувь':
        await message.answer('Выберите тип обуви', reply_markup=kb.children)
    elif message.text == 'Тапки':
        await message.answer('Выберите тип обуви', reply_markup=kb.slippers)
    elif message.text == 'Назад':
        await message.answer('Выберите категорию', reply_markup=kb.main)

