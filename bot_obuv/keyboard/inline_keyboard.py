from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


contact_and_address_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='\U0001F3D8, Наш адрес', callback_data='адрес'),
        InlineKeyboardButton(text='\U0000260E, Контакты', callback_data='телефон')

    ]
])



