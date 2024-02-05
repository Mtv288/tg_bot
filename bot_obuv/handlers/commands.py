from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.exceptions import TelegramBadRequest
from bot_obuv.keyboard.reply_keyboard import main_kb
from bot_obuv.data_base.data_base_main import update_user_visits

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Здравствуйте {message.from_user.full_name}')
    await message.answer('Я ваш виртуальный помощник', reply_markup=main_kb())
    await update_user_visits(message.from_user.full_name)



@router.message(Command("clear"))
async def cmd_clear(message: Message, bot: Bot) -> None:
    try:
        for i in range(message.message_id, 10, -1):
            await bot.delete_message(message.from_user.id, i)
    except TelegramBadRequest as ex:
        if ex.message == "Bad Request: message to delete not found":
            await message.answer('Главное меню', reply_markup=main_kb())
