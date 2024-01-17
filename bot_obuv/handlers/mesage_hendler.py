from aiogram import Router
from aiogram.types import Message


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
