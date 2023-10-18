import asyncio

from aiogram import Bot, Dispatcher, F, types
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
