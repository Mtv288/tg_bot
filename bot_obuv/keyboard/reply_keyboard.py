from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мужская обувь'),
            KeyboardButton(text='Женская обувь')
        ], [
            KeyboardButton(text='Детская обувь'),
            KeyboardButton(text='Тапочки')
        ]
    ], resize_keyboard=True,
    input_field_placeholder='Нажмите нужную кнопку'
)


men_kb = ReplyKeyboardMarkup(
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


women_kb = ReplyKeyboardMarkup(
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


child_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Туфли'),
            KeyboardButton(text='Ботинки')
        ], [
            KeyboardButton(text='Назад')
        ]
    ], resize_keyboard=True
)

slipper_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мужские'),
            KeyboardButton(text='Женские')
        ], [
            KeyboardButton(text='Назад')
        ]
    ], resize_keyboard=True
)

return_kb = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text='В раздел мужские'),
        KeyboardButton(text='В главное меню')
    ]], resize_keyboard=True
)
