from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.callback_query import CallbackQuery
from aiogram import Router
from aiogram.types import Message

select_type_shoes_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Наш адрес', callback_data='адрес'),
        InlineKeyboardButton(text='Контакты', callback_data='телефон')

    ]
])



