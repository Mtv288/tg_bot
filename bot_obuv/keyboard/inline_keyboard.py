from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


contact_and_address_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Наш адрес', callback_data='адрес'),
        InlineKeyboardButton(text='Контакты', callback_data='телефон')

    ]
])



