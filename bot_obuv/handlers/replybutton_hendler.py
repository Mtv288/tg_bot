from aiogram import F, Router, Bot, types
from aiogram.types import Message, InputFile, input_media
from sqlalchemy.orm import Session
from bot_obuv.data_base.data_base_main import Catalog, engine, CatalogAll
from bot_obuv.main_run import bot
from bot_obuv.keyboard.reply_keyboard import main_kb, men_kb, women_kb, \
    slipper_kb, return_kb_men, child_kb, return_kb_women, return_kb_children, return_kb_slippers, men_size_kb, \
    men_sport_shoes_kb, men_boots_size_kb, men_short_boots_size_kb, men_sabo_size_kb, kids_shoes_size_kb, \
    kids_boots_size_kb, women_shoes_kb, women_sabo_kb, women_boots_kb

from bot_obuv.data_base.data_base_main import list_name_goods, get_price_and_size_good_and_photo
import traceback, asyncio
from aiogram.filters import Command
from bot_obuv.data_base.data_base_main import update_user_visits, get_price_size_quantity, list_size_men, \
    get_list_media_group_file, \
    get_types_and_size_shoes, get_list_class_object_goods, split_list
from bot_obuv.keyboard.inline_keyboard import contact_and_address_kb

router = Router()

dict_type_shoes = [{'Тм': 'МУЖ П/Б'}, {'Км': 'МУЖ КРО'}, {'Тж': 'ЖЕН ТУФ'},
                   {'См': 'МУЖ САП'}, {'Бм': 'МУЖ БОТ'}, {'Мс': ('МУЖ САБ', 'МУЖ САН')},
                   {'Тд': 'ДЕТ П/Б'}, {'Бд': ['ДЕТ БОТ', 'ДЕТ САП']}, {'Тж': 'ЖЕН ТУФ'},
                   {'Сж': 'ЖЕН САБ'}, {'Бж': ['ЖЕН БОТ', 'ЖЕН САП', 'ЖЕН П/С']}]

list_word_address = ['ехать', 'находит', 'найти', 'адрес', 'телеф', 'связ', 'звон']


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
                price.append(get_price_size_quantity(i.name))
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
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Мужская обувь')
async def men(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=men_kb())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Женская обувь')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=women_kb())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Детская обувь')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=child_kb())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Тапки')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=slipper_kb())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Туфли Мужские')
async def men_size(message: Message):
    await message.delete()
    await message.answer('Туфли', reply_markup=men_size_kb())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'Тм. Смотреть все размеры')
async def men_shoes_list(message: Message):
    await message.delete()
    await message.answer('Туфли', reply_markup=return_kb_men())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_men())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Кроссовки Мужские')
async def men_size(message: Message):
    await message.delete()
    await message.answer('Кроссовки', reply_markup=men_sport_shoes_kb())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'Км. Смотреть все размеры')
async def men_shoes_list(message: Message):
    await message.delete()
    await message.answer('Кроссовки мужские', reply_markup=return_kb_men())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_men())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Мужские тапки')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_slippers())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_slippers())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Мужское Сабо')
async def men_size(message: Message):
    await message.delete()
    await message.answer('Сабо', reply_markup=men_sabo_size_kb())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'Мс. Смотреть все размеры')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_men())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_men())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Ботинки Мужские')
async def men_size(message: Message):
    await message.delete()
    await message.answer('Ботинки', reply_markup=men_short_boots_size_kb())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'Бм. Смотреть все размеры')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_men())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_men())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Сапоги Мужские')
async def men_size(message: Message):
    await message.delete()
    await message.answer('Сапоги', reply_markup=men_boots_size_kb())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'См. Смотреть все размеры')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_men())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_men())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Сапоги, Ботинки')
async def men_size(message: Message):
    await message.delete()
    await message.answer('Сапоги, Ботинки', reply_markup=women_boots_kb())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'Бж Смотреть все размеры')
async def men_shoes_list(message: Message):
    await message.delete()
    await message.answer('Сапоги, Ботинки', reply_markup=return_kb_women())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_women())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Туфли Женские')
async def men_size(message: Message):
    await message.delete()
    await message.answer('Туфли', reply_markup=women_shoes_kb())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'Тж Смотреть все размеры')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_women())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_women())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'Сабо Женское')
async def men_size(message: Message):
    await message.delete()
    await message.answer('Сабо', reply_markup=women_sabo_kb())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'Сж Смотреть все размеры')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_women())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_women())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Женские тапки')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_slippers())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_slippers())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Туфли Детские')
async def men_size(message: Message):
    await message.delete()
    await message.answer('Туфли', reply_markup=kids_shoes_size_kb())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'Тд. Смотреть все размеры')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_children())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_children())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Ботинки Детские')
async def men_size(message: Message):
    await message.delete()
    await message.answer('Ботинки', reply_markup=kids_boots_size_kb())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'Бд. Смотреть все размеры')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_children())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_children())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Детские тапки')
async def women(message: Message):
    await message.delete()
    await message.answer('Выберите категорию', reply_markup=return_kb_slippers())
    repp = await message.answer('Подождите идет загрузка фото')
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
    rep = await message.answer('Это весь ассортимент в данной категории')
    await asyncio.sleep(5)
    await rep.delete()
    await repp.delete()
    await message.answer('Главное меню', reply_markup=return_kb_slippers())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'В раздел мужские')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Раздел мужские', reply_markup=men_kb())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'В главное меню')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Главное меню', reply_markup=main_kb())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'В раздел женские')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Раздел женские', reply_markup=women_kb())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'В раздел детские')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Раздел Детские', reply_markup=child_kb())
    await  update_user_visits(message.from_user.full_name)


@router.message(F.text == 'В раздел тапки')
async def men_menu(message: Message):
    await message.delete()
    await message.answer('Раздел Детские', reply_markup=slipper_kb())
    await update_user_visits(message.from_user.full_name, message.from_user.id)


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
        await update_user_visits(message.from_user.full_name, message.from_user.id)


    else:
        rep = await message.reply('Нет в наличии')
        if rep:
            await asyncio.sleep(10)
            await message.delete()

    await message.answer('Главное меню', reply_markup=main_kb())
    await update_user_visits(message.from_user.full_name, message.from_user.id)
    await message.delete()


@router.message(F.text == 'Помощь.')
async def slippers(message: Message):
    rep = await message.reply('Это небольшая инструкция, как пользоваться помощником в чате. '
                              'Внизу Вы видите кнопки с разделами, нажимая на них Вы переходите в соответствующие разделы, '
                              'позволяющие выбрать интересующий Вас род и вид обуви, посмотреть фото и цены '
                              '(без учета скидочной карты покупателя на кожаную обувь). Все фото и цены актуальны! '
                              'Автоматически выводится наличие товара по размерам на тот момент, когда Вы запрашиваете информацию. '
                              'Если Вас интересует определенная модель обуви, то в поле сообщения наберите номер модели в формате "00-000", '
                              'который находится на фото и выглядит, например, так: "99-675". Или можно просто набрать сообщение,'
                              'допустим: "Мужские туфли", сразу выйдет меню с разделами мужской обуви:')

    await message.answer('Главное меню', reply_markup=main_kb())
    if rep:
        await asyncio.sleep(45)
        await rep.delete()
        await message.delete()
        await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message()
async def no_answer(message: Message):
    if message.text[:2] in [key for subdict in dict_type_shoes for key in subdict]:
        for i in dict_type_shoes:
            key = str(list(i.keys())[0])
            if key == message.text[:2] and len(message.text) == 8:
                type_shoes, size_sho = get_types_and_size_shoes(dict_type_shoes, message.text)
                list_obj = get_list_class_object_goods(CatalogAll, type_shoes, size_shoes=str(size_sho))
                lists_list_media_group_file = split_list(get_list_media_group_file(list_obj), 10)
                if lists_list_media_group_file:
                    rep = await message.reply('Подождите фото загружается')
                    for i in lists_list_media_group_file:
                        await bot.send_media_group(message.chat.id, media=i)
                    end = await message.answer('Это весь асортимент в этой категории')
                    await asyncio.sleep(10)
                    await rep.delete()
                    await end.delete()
                    await message.delete()
                    await update_user_visits(message.from_user.full_name, message.from_user.id)

                else:
                    ans = await message.answer('Нет в наличии')
                    await asyncio.sleep(10)
                    await ans.delete()
                    await message.delete()
                    await rep.delete()
                    await update_user_visits(message.from_user.full_name, message.from_user.id)

    elif any(word in message.text.lower() for word in list_word_address ):
        rep = await message.reply('Если вы хотите узнать наш адрес и контакты '
                                  'нажмите нужную кнопку под сообщением', reply_markup=contact_and_address_kb)
        await message.answer('Главное меню', reply_markup=main_kb())
        await asyncio.sleep(20)
        await message.delete()
        if rep:
            await rep.delete()
            await update_user_visits(message.from_user.full_name, message.from_user.id)