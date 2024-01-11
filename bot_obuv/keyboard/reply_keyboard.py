from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_kb():
    main = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Мужская обувь'),
                KeyboardButton(text='Женская обувь')
            ], [
                KeyboardButton(text='Детская обувь'),
                KeyboardButton(text='Тапки')
            ]
        ], resize_keyboard=True,
        input_field_placeholder='Нажмите нужную кнопку'
    )
    return main


def men_kb():
    men = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Туфли'),
                KeyboardButton(text='Ботинки')
            ],
            [
                KeyboardButton(text='Кроссовки'),
                KeyboardButton(text='Сабо')
            ],
            [
                KeyboardButton(text='Назад')
            ]
        ], resize_keyboard=True
    )
    return men


def women_kb():
    women = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Туфли'),
                KeyboardButton(text='Сапоги, Ботинки')
            ], [
                KeyboardButton(text='Сабо'),
                KeyboardButton(text='Назад')
            ]
        ], resize_keyboard=True
    )
    return women


def child_kb():
    child = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Туфли'),
                KeyboardButton(text='Ботинки')
            ], [
                KeyboardButton(text='Назад')
            ]
        ], resize_keyboard=True
    )
    return child


def slipper_kb():
    slipper = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Мужские'),
                KeyboardButton(text='Женские')
            ], [
                KeyboardButton(text='Назад')
            ]
        ], resize_keyboard=True
    )
    return slipper


def return_kb():
    return_b = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text='В раздел мужские'),
            KeyboardButton(text='В главное меню')
        ]], resize_keyboard=True
    )
    return return_b
