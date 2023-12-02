from aiogram import F, Router
from aiogram.types import Message
from bot.keyboard import reply_keyboard, inline_keyboard
from aiogram.types import FSInputFile
from sqlalchemy.orm import Session
from bot.data_base.data_base_main import Catalog
from bot.data_base.data_base_main import engine

router = Router()


@router.message(F.text == 'Назад')
async def back(message: Message):
    await message.delete()
    await message.answer('Главное меню', reply_markup=reply_keyboard.main_kb)


@router.message(F.text == 'Мужская обувь')
async def men(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=reply_keyboard.men_kb)


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


@router.message(F.text == 'Туфли')
async def men_shoes_list(message: Message):
    await message.answer('Назад', reply_markup=reply_keyboard.return_kb)
    with Session(engine) as session:
        for i in session.query(Catalog):
            await message.answer_photo(FSInputFile(str(i.photo)), f'Цена: {str(i.price)} р.', reply_markup=inline_keyboard.men)




@router.message(F.text == 'В раздел мужские')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('В раздел мужские', reply_markup=reply_keyboard.men_kb)


@router.message(F.text == 'В главное меню')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('В главное меню', reply_markup=reply_keyboard.main_kb)











