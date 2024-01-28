from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot_obuv.data_base.data_base_main import select_shoes_type, Catalog
callback_dat = select_shoes_type(Catalog, 'осен')
select_type_shoes_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Мужские', callback_data='Запарил'),
        InlineKeyboardButton(text='Женские', callback_data='khk'),
        InlineKeyboardButton(text='Детские', callback_data='gfghf')
    ]
])
