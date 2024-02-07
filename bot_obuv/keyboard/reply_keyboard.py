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
            ], [
                KeyboardButton(text='Помощь.')
            ]
        ], resize_keyboard=True,
        input_field_placeholder='Нажмите нужную кнопку'
    )
    return main


def men_kb():
    men = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Туфли Мужские'),
                KeyboardButton(text='Ботинки Мужские')
            ],
            [
                KeyboardButton(text='Кроссовки Мужские'),
                KeyboardButton(text='Сабо Мужское')
            ],
            [
                KeyboardButton(text='Сапоги Мужские'),
                KeyboardButton(text='Назад')
            ]
        ], resize_keyboard=True
    )
    return men


def women_kb():
    women = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Туфли Женские'),
                KeyboardButton(text='Сапоги, Ботинки')
            ], [
                KeyboardButton(text='Сабо Женское'),
                KeyboardButton(text='Назад')
            ]
        ], resize_keyboard=True
    )
    return women


def child_kb():
    child = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Туфли Детские'),
                KeyboardButton(text='Ботинки Детские')
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
                KeyboardButton(text='Мужские тапки'),
                KeyboardButton(text='Женские тапки')
            ], [
                KeyboardButton(text=' Детские тапки'),
                KeyboardButton(text='Назад')
            ]
        ], resize_keyboard=True
    )
    return slipper


def return_kb_men():
    return_b = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text='В раздел мужские'),
            KeyboardButton(text='В главное меню')
        ]], resize_keyboard=True
    )
    return return_b


def return_kb_women():
    return_b = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text='В раздел женские'),
            KeyboardButton(text='В главное меню')
        ]], resize_keyboard=True
    )
    return return_b


def return_kb_children():
    return_b = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text='В раздел детские'),
            KeyboardButton(text='В главное меню')
        ]], resize_keyboard=True
    )
    return return_b


def return_kb_slippers():
    return_b = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text='В раздел тапки'),
            KeyboardButton(text='В главное меню')
        ]], resize_keyboard=True
    )
    return return_b

