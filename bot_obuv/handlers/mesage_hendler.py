from aiogram import F, Router
from aiogram.types import Message
from bot_obuv.keyboard.inline_keyboard import select_type_shoes_kb
from aiogram.fsm.context import FSMContext
from bot_obuv.keyboard.reply_keyboard import main_kb, women_kb, men_kb, child_kb, slipper_kb
import asyncio
router = Router()


def answer_for_message(type_shoes):
    answer = f'Если вы хотите посмотреть ассортимент обуви нажмите на кнопку ' \
             f'{type_shoes} внизу экрана и выберите интересующую вас категорию обуви'
    return answer


@router.message(lambda message: 'жен' in message.text.lower())
async def woman_shoes(message: Message):
    reply = await message.reply(answer_for_message('"Женская обувь"'))
    await message.answer('Женская обувь', reply_markup=women_kb())
    await message.delete()
    await asyncio.sleep(10)
    if reply:
        await reply.delete()


@router.message(lambda message: 'муж' in message.text.lower())
async def men_shoes(message: Message):
    reply = await message.reply(answer_for_message('"Мужская обувь"'))
    await message.answer('Мужская обувь', reply_markup=men_kb())
    await message.delete()
    await asyncio.sleep(10)
    if reply:
        await reply.delete()


@router.message(lambda message: 'дет' in message.text.lower())
async def kid_shoes(message: Message):
    reply = await message.reply(answer_for_message('"Детская обувь"'))
    await message.answer('Детская обувь', reply_markup=child_kb())
    await message.delete()
    await asyncio.sleep(10)
    if reply:
        await reply.delete()


@router.message(lambda message: 'тап' in message.text.lower())
async def slippers(message: Message):
    reply = await message.reply(answer_for_message('"Тапки"'))
    await message.answer('Тапки', reply_markup=slipper_kb())
    await message.delete()
    await asyncio.sleep(10)
    if reply:
        await reply.delete()


@router.message(lambda message: 'работа' in message.text.lower())
async def job_time(message: Message):
    await message.reply('_____Наш режим работы:_____'
                        '  Понедельник - Пятница с 8.00 до 17.30'
                        '  Суббота - Воскресенье с 9.00 до 16.00'
                        '  без перерывов и выходных')


@router.message(F.text == 'Помощь.')
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
async def price(message: Message):
    for i in ['цен', 'стоит', 'почем']:
        if i in message.text.lower():
            await message.reply('Чтобы узнать цену и наличие размеров, '
                                'введите артикул модели который находится на фото и '
                                'выглядит в таком формате "99-999".(Вместо девяток подставьте нужные цифры) ')


