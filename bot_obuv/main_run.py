import asyncio
import logging
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from handlers import commands, replybutton_hendler, mesage_hendler, inline_handlers
from bot_obuv.data_base.data_base_main import update_all_tables
import schedule
import time

load_dotenv()
bot = Bot(os.getenv('TOKEN'))


async def start():

    logging.basicConfig(filename='logs.log', level=logging.ERROR)
    dp = Dispatcher()
    dp.include_router(commands.router)
    dp.include_router(replybutton_hendler.router)
    dp.include_router(inline_handlers.router)
    dp.include_router(mesage_hendler.router)
    await dp.start_polling(bot)
    schedule.every().hour.do(update_all_tables)

schedule.every().hour.do(update_all_tables)


async def run_schedule():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(run_schedule(), start()))

