from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main_keyboard = [[KeyboardButton(text='Мужская обувь'), KeyboardButton(text='Женская обувь')],
                 [KeyboardButton(text='Детская обувь'), KeyboardButton(text='Тапки')]]

mens_footwear = [[KeyboardButton(text='Туфли'), KeyboardButton(text='Ботинки')],
                 [KeyboardButton(text='Кроссовки'), KeyboardButton(text='Назад')]]

mens = ReplyKeyboardMarkup(keyboard=mens_footwear,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

main = ReplyKeyboardMarkup(keyboard=main_keyboard,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')
