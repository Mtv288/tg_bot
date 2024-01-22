import asyncio
from aiogram import Bot, Dispatcher, types
import os
from dotenv import load_dotenv
from handlers import commands, replybutton_hendler, mesage_hendler
from bot_env import bot





async def start():
    dp = Dispatcher()
    dp.include_router(commands.router)
    dp.include_router(replybutton_hendler.router)
    dp.include_router(mesage_hendler.router)
    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(start())

