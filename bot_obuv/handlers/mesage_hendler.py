from aiogram import Router, F
from aiogram.types import Message
from bot_obuv.data_base.data_base_main import list_name_goods, get_price_and_size_good_and_photo
from aiogram import F, Router
from aiogram.types import Message, InputFile, input_media
from sqlalchemy.orm import Session
from bot_obuv.data_base.data_base_main import Catalog
from bot_obuv.data_base.data_base_main import engine
from aiogram import types
from bot_obuv.main_run import bot
from bot_obuv.keyboard.reply_keyboard import main_kb, men_kb, women_kb, \
    slipper_kb, return_kb_men, child_kb, return_kb_women, return_kb_children, return_kb_slippers
from bot_obuv.data_base.data_base_main import list_name_goods, get_price_and_size_good_and_photo

router = Router()


def answer_for_message(type_shoes):
    answer = f'Если вы хотите посмотреть ассортимент обуви нажмите на кнопку ' \
             f'{type_shoes} внизу экрана и выберите интересующую вас категорию обуви'
    return answer


@router.message(lambda message: 'жен' in message.text.lower())
async def woman_shoes(message: Message):
    await message.reply(answer_for_message('"Женская обувь"'))


@router.message(lambda message: 'муж' in message.text.lower())
async def men_shoes(message: Message):
    await message.reply(answer_for_message('"Мужская обувь"'))


@router.message(lambda message: 'дет' in message.text.lower())
async def kid_shoes(message: Message):
    await message.reply(answer_for_message('"Детская обувь"'))


@router.message(lambda message: 'тап' in message.text.lower())
async def slippers(message: Message):
    await message.reply(answer_for_message('"Тапки"'))


@router.message(lambda message: 'работа' in message.text.lower())
async def job_time(message: Message):
    await message.reply('_____Наш режим работы:_____'
                        '  Понедельник - Пятница с 8.00 до 17.30'
                        '  Суббота - Воскресенье с 9.00 до 16.00'
                        '  без перерывов и выходных')


@router.message(F.text == 'Помощь')
async def slippers(message: Message):
    await message.reply('Это небольшая инструкция как пользоваться помощником в чате')
    await message.reply('Внизу вы видите кнопки с разделами, нажимая на них вы переходите в соответсвующие разделы '
                        'позволяющие выбрать интересующий вас тип обуви и посмотреть фото и цены,'
                        'все фото и цены актуальны показано то что есть в наличии на момент когда вы смотрите')
    await message.reply('Если вас интересует определенная модель обуви, то в поле сообщение наберите '
                        'код модели, например "99-555", код модели находится на фото и выглядит как "ЧЧ-ЧЧЧ"')
    await message.reply('Или можно просто набрать сообщение допустим "мужские летние"')
    await message.delete()


@router.message()
async def check_for_rt(message: Message):
    rt = list_name_goods()
    count = 0
    for word in rt:
        if word in message.text.lower():
            count += 1
            break
    if count > 0:
        list_size_str, phot, price = get_price_and_size_good_and_photo(word)
        r = types.FSInputFile(phot)
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=r)
        await message.reply(f'Цена: {price}р. {list_size_str}')

    else:
        await message.reply('Нет в наличии')


@router.message()
async def none_text(message: Message):
    await message.reply('Я вас не понял повторите вопрос более корректно')
