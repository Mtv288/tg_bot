from aiogram import F, Router
from aiogram.types import Message
from bot_obuv.keyboard.reply_keyboard import main_kb, women_kb, men_kb, child_kb, slipper_kb
import asyncio
from bot_obuv.keyboard.inline_keyboard import contact_and_address_kb
from bot_obuv.data_base.data_base_main import update_user_visits

list_price_text = ['цен', 'стоит', 'почем', 'размер']


router = Router()

answer = 'Если вы хотите посмотреть ассортимент обуви нажмите на  нужную кнопку ' \
         'внизу экрана'


@router.message(lambda message: 'жен' in message.text.lower())
async def woman_shoes(message: Message):
    reply = await message.reply(answer)
    await message.answer('Женская обувь', reply_markup=women_kb())
    await update_user_visits(message.from_user.full_name)
    await asyncio.sleep(10)
    await message.delete()
    if reply:
        await reply.delete()
        await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(lambda message: 'муж' in message.text.lower())
async def men_shoes(message: Message):
    reply = await message.reply(answer)
    await message.answer('Мужская обувь', reply_markup=men_kb())
    await asyncio.sleep(10)
    await message.delete()
    if reply:
        await reply.delete()
        await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(lambda message: 'дет' in message.text.lower())
async def kid_shoes(message: Message):
    reply = await message.reply(answer)
    await message.answer('Детская обувь', reply_markup=child_kb())
    await asyncio.sleep(10)
    await message.delete()
    if reply:
        await reply.delete()
        await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(lambda message: 'тап' in message.text.lower())
async def slippers(message: Message):
    reply = await message.reply(answer)
    await message.answer('Тапки', reply_markup=slipper_kb())
    await asyncio.sleep(10)
    await message.delete()
    if reply:
        await reply.delete()
        await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(lambda message: 'работа' in message.text.lower())
async def job_time(message: Message):
    rep = await message.reply('_____Наш режим работы:_____'
                              '  Понедельник - Пятница с 8.00 до 17.30'
                              '  Суббота - Воскресенье с 9.00 до 16.00'
                              '  без перерывов и выходных')
    if rep:
        await asyncio.sleep(15)
        await message.delete()
        await rep.delete()
        await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message(F.text == 'Спасибо')
async def reply_to_thank_you(message: Message):
    rep = await message.reply('Пожалуйста, рад что смог помочь')
    if rep:
        await asyncio.sleep(10)
        await rep.delete()
        await message.delete()
        await update_user_visits(message.from_user.full_name, message.from_user.id)


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
        await update_user_visits(message.from_user.full_name, message.from_user.id)


@router.message()
async def no_answer(message: Message):
    if len(message.text) >= 9 and len(message.text) != 6:
        rep = await message.reply('Извините я не понял вопрос')
        await message.answer('Главное меню', reply_markup=main_kb())
        if rep:
            await asyncio.sleep(10)
            await rep.delete()
            await message.delete()
            await update_user_visits(message.from_user.full_name, message.from_user.id)


