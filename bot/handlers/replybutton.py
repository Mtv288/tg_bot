from aiogram import F, Router
from aiogram.types import Message
from bot.keyboard import reply_keyboard
from bot.keyboard import inline_keyboard
from aiogram.types import FSInputFile



router = Router()


@router.message(F.text == 'Назад')
async def back(message: Message):
    await message.delete()
    await message.answer('Главное меню', reply_markup=reply_keyboard.main_kb)


@router.message(F.text == 'Мужская обувь')
async def men(message: Message):
    await message.delete()
    await message.answer_photo(FSInputFile('Y:\\Обувь\\Photo\\10309.jpg'))
    await message.answer('Выберите категорию', reply_markup=inline_keyboard.men)


@router.message(F.text == 'Женская обувь')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=reply_keyboard.women_kb)


@router.message(F.text == 'Детская обувь')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=reply_keyboard.child_kb)


@router.message(F.text == 'Тапочки')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=reply_keyboard.slipper_kb)
