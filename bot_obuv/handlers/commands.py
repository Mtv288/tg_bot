from aiogram import Router, types
from aiogram.types import Message
from bot_obuv.keyboard.reply_keyboard import main_kb
from aiogram.filters import CommandStart
from sqlalchemy.orm import Session
from bot_obuv.data_base.data_base_main import engine
from bot_obuv.data_base.data_base_main import MessageHistory


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Здравствуйте {message.from_user.first_name}')
    await message.answer('Я ваш виртуальный помощник', reply_markup=main_kb())


@router.message()
async def handle_message(message: types.Message):
    with Session(engine) as session:
        chat_message = MessageHistory(user_chat_id=message.from_user.id, user_message_id=message.message_id)
        session.add(chat_message)
        session.commit()








