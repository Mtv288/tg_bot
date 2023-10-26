import asyncio
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from handlers import commands, replybutton_hendler



load_dotenv()


async def start():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(commands.router)
    dp.include_router(replybutton_hendler.router)




    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
