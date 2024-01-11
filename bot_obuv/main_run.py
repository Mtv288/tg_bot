import asyncio
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from handlers import commands, replybutton_hendler, mesage_hendler

load_dotenv()
bot = Bot(os.getenv('TOKEN'))


async def start():
    dp = Dispatcher()
    dp.include_router(commands.router)
    dp.include_router(replybutton_hendler.router)
    dp.include_router(mesage_hendler.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
