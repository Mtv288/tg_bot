from aiogram import Bot, Dispatcher, F
import asyncio
from aiogram.types import Message
from app.handlers import router
import keyboar as kb


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать', reply_markup=kb.main)


async def main():
    bot = Bot(token='6247171392:AAEQ1gb798E2DLx9IvLJ1yxgGs3du-OHekE')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
