from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


select_type_shoes_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Мужские', callback_data='Запарил'),
        InlineKeyboardButton(text='Женские', callback_data='khk'),
        InlineKeyboardButton(text='Детские', callback_data='gfghf')
    ]
])
