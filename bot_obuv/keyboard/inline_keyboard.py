from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.callback_query import CallbackQuery

men = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Размеры в наличии', callback_data='ryrty')
    ]
])
