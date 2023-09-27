from aiogram import Bot, Dispatcher, F
import asyncio
from aiogram.types import Message

bot = Bot(token='6247171392:AAEQ1gb798E2DLx9IvLJ1yxgGs3du-OHekE')
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать')


async def main():
    await dp.start_polling(bot)


asyncio.run((main()))

if __name__== '__main__':
    asyncio.run(main())

