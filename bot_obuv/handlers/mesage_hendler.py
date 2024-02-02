from aiogram import F, Router
from aiogram.types import Message
from bot_obuv.keyboard.reply_keyboard import main_kb, women_kb, men_kb, child_kb, slipper_kb
import asyncio
from bot_obuv.keyboard.inline_keyboard import contact_and_address_kb

list_price_text = ['цен', 'стоит', 'почем']
list_word_address = ['как', 'ехать', 'где', 'найти', 'адрес']

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
    await message.delete()


@router.message(F.text == 'Помощь.')
async def slippers(message: Message):
    rep = await message.reply('Это небольшая инструкция как пользоваться помощником в чате. '
                              'Внизу вы видите кнопки с разделами, нажимая на них вы переходите в соответствующие разделы '
                              'позволяющие выбрать интересующий вас тип обуви и посмотреть фото и цены,'
                              'все фото и цены актуальны показано то что есть в наличии на момент когда вы смотрите. '
                              'Если вас интересует определенная модель обуви, то в поле сообщение наберите '
                              'код модели, например "99-555", код модели находится на фото и выглядит как "ЧЧ-ЧЧЧ". '
                              'Или можно просто набрать сообщение допустим "мужские туфли"')

    await message.answer('Главное меню', reply_markup=main_kb())
    if rep:
        await asyncio.sleep(45)
        await rep.delete()
        await message.delete()


@router.message(F.text == 'Спасибо')
async def reply_to_thank_you(message: Message):
    rep = await message.reply('Пожалуйста, рад что смог помочь')
    if rep:
        await asyncio.sleep(10)
        await rep.delete()
        await message.delete()


@router.message(lambda message: any(word in message.text.lower() for word in list_word_address))
async def search_type_shoes(message: Message):
    rep = await message.reply('Если вы хотите узнать наш адрес и контакты '
                              'нажмите нужную кнопку под сообщением', reply_markup=contact_and_address_kb)
    await message.answer('Главое меню', reply_markup=main_kb())
    await asyncio.sleep(20)
    await message.delete()
    if rep:
        await rep.delete()


@router.message(lambda message: any(word in message.text.lower() for word in list_price_text))
async def price(message: Message):
    rep = await message.reply('Чтобы узнать цену и наличие размеров, '
                              'введите артикул модели который находится на фото и '
                              'выглядит в таком формате "99-999".(Вместо девяток подставьте нужные цифры) ')
    await message.answer('Главное меню', reply_markup=men_kb())
    await asyncio.sleep(10)
    await message.delete()
    if rep:
        await rep.delete()


@router.message()
async def no_answer(message: Message):
    if len(message.text) != 6:
        rep = await message.reply('Извините я не понял вопрос')
        await message.delete()
        await message.answer('Главное меню', reply_markup=main_kb())
        if rep:
            await asyncio.sleep(8)
            await rep.delete()
