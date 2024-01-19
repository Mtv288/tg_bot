from aiogram import F, Router
from aiogram.types import Message
from sqlalchemy.orm import Session
from bot_obuv.data_base.data_base_main import Catalog
from bot_obuv.data_base.data_base_main import engine
from aiogram import types
from bot_obuv.main_run import bot
from bot_obuv.keyboard.reply_keyboard import main_kb, men_kb, women_kb, \
    slipper_kb, return_kb_men, child_kb, return_kb_women

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


@router.message(F.text == 'Тапки.')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=slipper_kb())


@router.message(F.text == 'Туфли')
async def men_shoes_list(message: Message):
    await message.delete()
    await message.answer('Туфли', reply_markup=return_kb_men())
    photos, price, count_message_for_media_group = create_list_for_media_group('МУЖ П/Б')

    if count_message_for_media_group == 1:
            creat_list_media_no_more_than_10(photos, price, count_message_for_media_group)
            await bot.send_media_group(message.chat.id,
                                       media=creat_list_media_no_more_than_10(photos, price, count_message_for_media_group))
            count_message_for_media_group = 0
    else:
        for _ in range(count_message_for_media_group):
            photo = photos
            prices = price
            med = [types.InputMediaPhoto(media=photo, caption=prices) for photo, prices in zip(photo[:10], prices[:10])]
            await bot.send_media_group(message.chat.id, media=med)
            del photo[0: 10]
            del prices[0: 10]


@router.message(F.text == 'Кроссовки.')
async def men_shoes_list(message: Message):
    await message.delete()
    await message.answer('Кроссовки мужские', reply_markup=return_kb_men())
    photos, price, count_message_for_media_group = create_list_for_media_group('МУЖ КРО')

    for _ in range(count_message_for_media_group):
        photo = photos
        prices = price
        med = [types.InputMediaPhoto(media=photo, caption=prices) for photo, prices in zip(photo[:10], prices[:10])]
        await bot.send_media_group(message.chat.id, media=med)
        del photo[0: 10]
        del prices[0: 10]


@router.message(F.text == 'Сапоги, Ботинки')
async def men_shoes_list(message: Message):
    await message.delete()
    await message.answer('Сапоги, Ботинки', reply_markup=return_kb_women())
    photos, price, count_message_for_media_group = create_list_for_media_group(['ЖЕН БОТ', 'ЖЕН САП', 'ЖЕН П/С'])
    if count_message_for_media_group == 1:
        creat_list_media_no_more_than_10(photos, price)
        await bot.send_media_group(message.chat.id, media=creat_list_media_no_more_than_10(photos, price))

    else:
        for _ in range(count_message_for_media_group):
            photo = photos
            prices = price
            med = [types.InputMediaPhoto(media=photo, caption=prices) for photo, prices in zip(photo[:10], prices[:10])]
            await bot.send_media_group(message.chat.id, media=med)
            del photo[0: 10]
            del prices[0: 10]


@router.message(F.text == 'В раздел мужские')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Раздел мужские', reply_markup=men_kb())


@router.message(F.text == 'В главное меню')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Главное меню', reply_markup=main_kb())


@router.message(F.text == 'В раздел женские')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Раздел женские', reply_markup=women_kb())


def create_list_for_media_group(world=[]):
    photos = []
    price = []
    with Session(engine) as ses:
        for i in ses.query(Catalog):
            if i.name[:7] in world:
                photos.append(types.FSInputFile(i.photo))
                price.append(f'Цена {str(i.price)}р.')
        count_message_for_media_group = len(photos) / 10

        if not isinstance(count_message_for_media_group, int) and count_message_for_media_group != 1:
            count_message_for_media_group = int(count_message_for_media_group) + 1

        else:
            count_message_for_media_group = 1

    return photos, price, count_message_for_media_group


def creat_list_media_no_more_than_10(media_file, text_in_the_file):
    photo = media_file
    prices = text_in_the_file
    med = [types.InputMediaPhoto(media=photo, caption=prices) for photo, prices in zip(photo[:10], prices[:10])]
    return med


    # med = [types.InputMediaPhoto(media=photo, caption=prices) for photo, prices in zip(photo[:9], prices[:9])]
    # await bot.send_media_group(message.chat.id, media=med)
    # del photo[0: 10]
    # del prices[0: 10]
    count_message_for_media_group = 0
