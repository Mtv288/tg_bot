from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


select_type_shoes_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Наш адрес', callback_data='адрес'),
        InlineKeyboardButton(text='Контакты', callback_data='телефон')

    ]
])



