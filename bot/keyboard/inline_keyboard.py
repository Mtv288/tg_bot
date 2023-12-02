from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import F, Router
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery

men = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Цена', callback_data='gdfg'),
        InlineKeyboardButton(text='Размеры в наличии', callback_data='ryrty')
    ]
])
