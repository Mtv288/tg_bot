from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.callback_query import CallbackQuery

select_type_shoes_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Мужские', callback_data='ryrty'),
        InlineKeyboardButton(text='Женские', callback_data='khk')
    ]
])
