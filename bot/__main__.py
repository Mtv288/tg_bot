import asyncio

from aiogram import Bot, Dispatcher
import os
from commands import register_user_command


async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    register_user_command(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
