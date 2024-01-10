from aiogram import F, Router
from aiogram.types import Message
from bot_obuv.keyboard import inline_keyboard
from aiogram.types import FSInputFile
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
    photos, price = g('МУЖ П/Б')
    f = len(photos) // 10
    for _ in range(f + 1):
        p = photos
        pr = price
        med = [types.InputMediaPhoto(media=p, caption=pr) for p, pr in zip(p[:10], pr[:10])]
        await bot.send_media_group(message.chat.id, media=med)
        del p[0: 10]
        del pr[0: 10]



@router.message(F.text == 'Кроссовки')
async def men_shoes_list(message: Message):
    await message.answer('Назад', reply_markup=return_kb())
    photos, price = g('МУЖ КРО')
    f = len(photos) // 10
    for _ in range(f + 1):
        p = photos
        pr = price
        med = [types.InputMediaPhoto(media=p, caption=pr) for p, pr in zip(p[:10], pr[:10])]
        await bot.send_media_group(message.chat.id, media=med)
        del p[0: 10]
        del pr[0: 10]


@router.message(F.text == 'В раздел мужские')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('В раздел мужские', reply_markup=men_kb())


@router.message(F.text == 'В главное меню')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('В главное меню', reply_markup=main_kb())


def g(world):
    photos = []
    price = []
    with Session(engine) as ses:
        for i in ses.query(Catalog):
            if i.name[:7] == world:
                photos.append(types.FSInputFile(i.photo))
                price.append(f'Цена {str(i.price)}р.')
    return photos, price

