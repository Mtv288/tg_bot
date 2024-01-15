from aiogram import Router, Bot
from aiogram.types import Message
from bot_obuv.keyboard.reply_keyboard import main_kb
from aiogram.filters import CommandStart, Command
from aiogram.exceptions import TelegramBadRequest
router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Здравствуйте {message.from_user.first_name}')
    await message.answer('Я ваш виртуальный помощник', reply_markup=main_kb())

@router.message(Command("clear"))
async def cmd_clear(message: Message, bot: Bot) -> None:
    try:
        for i in range(message.message_id, 10, -1):
            await bot.delete_message(message.from_user.id, i)
    except TelegramBadRequest as ex:
        if ex.message == "Bad Request: message to delete not found":
            print("Все сообщения удалены")

