from aiogram import Bot, Dispatcher, F
import asyncio
from aiogram.types import Message

bot = Bot(token='6247171392:AAEQ1gb798E2DLx9IvLJ1yxgGs3du-OHekE')
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать')
    await message.answer('Я ваш помощник в чате')


@dp.message(F.text.lower() == 'как')
async def cm(message: Message):
    await message.answer(f'Здравствуйте {message.from_user.last_name}')


@dp.message()
async def eho(message: Message):
    await message.answer('Простите я вас не понимаю')


async def main():
    await dp.start_polling(bot)


asyncio.run((main()))

if __name__ == '__main__':
    asyncio.run(main())
