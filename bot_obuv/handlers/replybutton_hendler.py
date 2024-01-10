from aiogram import F, Router
from aiogram.types import Message
from bot_obuv.keyboard import reply_keyboard, inline_keyboard
from aiogram.types import FSInputFile, InputFile
from sqlalchemy.orm import Session
from bot_obuv.data_base.data_base_main import Catalog
from bot_obuv.data_base.data_base_main import engine
from aiogram import types
from bot_obuv.main_run import bot
from bot_obuv.keyboard.reply_keyboard import main_kb, men_kb, women_kb, slipper_kb, return_kb, child_kb


router = Router()


@router.message(F.text == 'Назад')
async def back(message: Message):
    await message.delete()
    await message.answer('Главное меню', reply_markup=main_kb())


@router.message(F.text == 'Мужская обувь')
async def men(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=men_kb())


@router.message(F.text == 'Женская обувь')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=women_kb())


@router.message(F.text == 'Детская обувь')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=child_kb())


@router.message(F.text == 'Тапочки')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=slipper_kb())


@router.message(F.text == 'Туфли')
async def men_shoes_list(message: Message):
    await message.delete()
    await message.answer('Назад', reply_markup=return_kb())
    photos = []
    price = []
    print(len(photos))
    with Session(engine) as ses:
        for i in ses.query(Catalog):
            if i.name[:7] == 'МУЖ П/Б':
                photos.append(types.FSInputFile(i.photo))
                price.append(f'Цена {str(i.price)}р.')
    med = [types.InputMediaPhoto(media=photo, caption=pr) for photo, pr in zip(photos[:10], price[:10])]
    await bot.send_media_group(message.chat.id, media=med)


@router.message(F.text == 'Кроссовки')
async def men_shoes_list(message: Message):
    await message.answer('Назад', reply_markup=return_kb())
    with Session(engine) as session:
        for i in session.query(Catalog):
            await message.answer_photo(FSInputFile(str(i.photo)), f'Цена: {str(i.price)} р.',
                                       reply_markup=inline_keyboard.men)


@router.message(F.text == 'В раздел мужские')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('В раздел мужские', reply_markup=men_kb())


@router.message(F.text == 'В главное меню')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('В главное меню', reply_markup=main_kb())
