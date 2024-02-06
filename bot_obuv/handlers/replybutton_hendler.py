from aiogram import F, Router, Bot
from aiogram.types import Message, InputFile, input_media
from sqlalchemy.orm import Session
from bot_obuv.data_base.data_base_main import Catalog
from bot_obuv.data_base.data_base_main import engine
from aiogram import types
from bot_obuv.main_run import bot
from bot_obuv.keyboard.reply_keyboard import main_kb, men_kb, women_kb, \
    slipper_kb, return_kb_men, child_kb, return_kb_women, return_kb_children, return_kb_slippers
from bot_obuv.data_base.data_base_main import list_name_goods, get_price_and_size_good_and_photo
from bot_obuv.main_run import bot
import traceback
from aiogram.filters import Command
import asyncio
from bot_obuv.data_base.data_base_main import update_user_visits

router = Router()


def create_list_for_media_group(world=[]):
    """
    Функция собирает два списка для фотографий и подписи под фото в данном случае это цена товара,
    затем делит на 10 что-бы получить количество циклов для отправки сообщений в каждом сообщение
    может быть не больше 10 файлов
    :param world: Сюда вписываем слово или его часть по которой будет производиться выборка из таблицы catalog,
    слов может быть несколько поэтому тут список
    :return: получаем список с фото список с текстом под фото и количество циклов для отправки сообщений в
    виде media_gruup
    """
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


def create_list_media_no_more_than_10(media_file, text_in_the_file):
    """
    Функция собирает 2 списка с фото и текстом под фото если таких обьектов меньше или равно 10
    :param media_file: Фото товара
    :param text_in_the_file: Подпись под фото(в данном случае цена)
    :return: обьект для отправки сообщения в виде media_grupp
    """
    photo = media_file
    prices = text_in_the_file
    med = [types.InputMediaPhoto(media=photo, caption=prices) for photo, prices in zip(photo[:10], prices[:10])]
    return med


def create_lists_media_group(media, text, count_message):
    """
    Функця собирает список обьектов типа media_grupp(не больше 10 в каждом списке) для отправки сообений
    :param media: фото товара
    :param text: подпись под фото(в данном случае цена)
    :param count_message: количество циклов для создания media_grupp
    :return: список готовых обьектов типа media_grupp
    """
    lists_list_melia_group = []
    for _ in range(count_message):
        photo = media
        prices = text
        med = [types.InputMediaPhoto(media=photo, caption=prices) for photo, prices in zip(photo[:10], prices[:10])]
        lists_list_melia_group.append(med)
        del photo[0: 10]
        del prices[0: 10]
    return lists_list_melia_group


@router.message(F.text == 'Назад')
async def back(message: Message):
    await message.delete()
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)



@router.message(F.text == 'Мужская обувь')
async def men(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=men_kb())
    await  update_user_visits(message.from_user.full_name)



@router.message(F.text == 'Женская обувь')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=women_kb())
    await  update_user_visits(message.from_user.full_name)



@router.message(F.text == 'Детская обувь')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=child_kb())
    await  update_user_visits(message.from_user.full_name)



@router.message(F.text == 'Тапки')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=slipper_kb())
    await  update_user_visits(message.from_user.full_name)



@router.message(F.text == 'Туфли Мужские')
async def men_shoes_list(message: Message):
    await message.delete()
    await message.answer('Туфли', reply_markup=return_kb_men())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group('МУЖ П/Б')
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Кроссовки Мужские')
async def men_shoes_list(message: Message):
    await message.delete()
    await message.answer('Кроссовки мужские', reply_markup=return_kb_men())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group('МУЖ КРО')
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Мужские тапки')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_slippers())
    count = 0
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group('Тапки м')
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Сабо Мужское')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_men())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group(['МУЖ САБ', 'МУЖ САН'])
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Ботинки Мужские')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_men())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group('МУЖ БОТ')
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Сапоги Мужские')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_men())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group('МУЖ САП')
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Сапоги, Ботинки')
async def men_shoes_list(message: Message):
    await message.delete()
    await message.answer('Сапоги, Ботинки', reply_markup=return_kb_women())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group(['ЖЕН БОТ', 'ЖЕН САП', 'ЖЕН П/С'])
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Туфли Женские')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_women())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group('ЖЕН ТУФ')
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Сабо Женское')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_women())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group('ЖЕН САБ')
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Женские тапки')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_slippers())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group('Тапки ж')
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Туфли Детские')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_children())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group('ДЕТ П/Б')
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Ботинки Детские')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_children())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group(['ДЕТ БОТ', 'ДЕТ САП'])
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.chat.id, media=i)

    except Exception as e:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()
    await asyncio.sleep(10)



@router.message(F.text == 'Детские тапки')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_slippers())
    try:
        photos, price, count_message_for_media_group = create_list_for_media_group('Тапки д')
        if count_message_for_media_group == 1:
            await bot.send_media_group(message.chat.id, media=create_list_media_no_more_than_10(photos, price))

        else:
            list_media_group = create_lists_media_group(photos, price, count_message_for_media_group)
            for i in list_media_group:
                await bot.send_media_group(message.from_user.id, media=i)
    except Exception:
        pass
    await message.answer('Это весь ассортимент в данной категории')
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)



@router.message(F.text == 'В раздел мужские')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Раздел мужские', reply_markup=men_kb())
    await  update_user_visits(message.from_user.full_name)



@router.message(F.text == 'В главное меню')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)



@router.message(F.text == 'В раздел женские')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Раздел женские', reply_markup=women_kb())
    await  update_user_visits(message.from_user.full_name)



@router.message(F.text == 'В раздел детские')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Раздел Детские', reply_markup=child_kb())
    await  update_user_visits(message.from_user.full_name)



@router.message(F.text == 'В раздел тапки')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Раздел Детские', reply_markup=slipper_kb())
    await  update_user_visits(message.from_user.full_name)




@router.message(F.text.len() == 6)
async def check_for_rt(message: Message):
    count = 0
    for word in list_name_goods():
        if word in message.text.lower():
            count += 1
            break
    if count > 0:
        list_size_str, phot, price = get_price_and_size_good_and_photo(word)
        photo_goods = types.FSInputFile(phot)
        await bot.send_photo(chat_id=message.chat.id,
                             photo=photo_goods)
        await message.reply(f'Цена: {price}р. {list_size_str}')
        await  update_user_visits(message.from_user.full_name)


    else:
        rep = await message.reply('Нет в наличии')
        if rep:
            await asyncio.sleep(10)
            await message.delete()

    await message.answer('Главное меню', reply_markup=main_kb())
    await  update_user_visits(message.from_user.full_name)
    await message.delete()


