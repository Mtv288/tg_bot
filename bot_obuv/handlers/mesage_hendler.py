from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: 'жен' in message.text.lower())
async def woman_shoes(message: Message):
    await message.reply('Если вы хотите посмотреть ассортимент женской обуви напишите '
                        '"Женская обувь" без кавычек ')


@router.message(lambda message: 'муж' in message.text.lower())
async def men_shoes(message: Message):
    await message.reply('Если вы хотите посмотреть ассортимент мужской обуви нажмите на кнопку '
                        '"Мужская обувь" внизу экрана и выберите интересующую вас категорию обуви')


@router.message(lambda message: 'дет' in message.text.lower())
async def kid_shoes(message: Message):
    await message.reply('Если вы хотите посмотреть ассортимент детской обуви нажмите на кнопку '
                        '"Детская обувь" внизу экрана и выберите интересующую вас категорию обуви')


@router.message(lambda message: 'тап' in message.text.lower())
async def slippers(message: Message):
    await message.reply('Если вы хотите посмотреть ассортимент тапочек нажмите на кнопку '
                        '"Тапки" внизу экрана и выберите интересующую вас категорию')


@router.message(lambda message: 'работа' in message.text.lower())
async def job_time(message: Message):
    await message.reply('Наш режим работы:'
                        '  Понедельник - Пятница с 8.00 до 17.30'
                        '  Суббота - Воскресенье с 9.00 до 16.00'
                        '  без перерывов и выходных')

