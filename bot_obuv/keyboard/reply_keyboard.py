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
                KeyboardButton(text='Помощь.'),
                KeyboardButton(text='График работы')
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
                KeyboardButton(text='Мужское Сабо')
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


def men_size_kb():
    shoes = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Тм. Смотреть все размеры')
            ], [
                KeyboardButton(text='Тм  р:39'),
                KeyboardButton(text='Тм  р:40'),
                KeyboardButton(text='Тм  р:41'),
                KeyboardButton(text='Тм  р:42'),
                KeyboardButton(text='Тм  р:43')

            ], [KeyboardButton(text='Тм  р:44'),
                KeyboardButton(text='Тм  р:45'),
                KeyboardButton(text='Тм  р:46'),
                KeyboardButton(text='Тм  р:47'),
                KeyboardButton(text='Тм  р:48')

                ], [
                KeyboardButton(text='В раздел мужские')
            ],
        ], resize_keyboard=True
    )
    return shoes


def men_sport_shoes_kb():
    sport_shoes = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Км. Смотреть все размеры')
            ], [
                KeyboardButton(text='Км  р:36'),
                KeyboardButton(text='Км  р:37'),
                KeyboardButton(text='Км  р:38'),
                KeyboardButton(text='Км  р:39'),
                KeyboardButton(text='Км  р:40')

            ], [
                KeyboardButton(text='Км  р:41'),
                KeyboardButton(text='Км  р:42'),
                KeyboardButton(text='Км  р:43'),
                KeyboardButton(text='Км  р:44'),
                KeyboardButton(text='Км  р:45')

            ], [
                KeyboardButton(text='Км  р:46'),
                KeyboardButton(text='Км  р:47'),
                KeyboardButton(text='Км  р:48'),
                KeyboardButton(text='Км  р:49'),
                KeyboardButton(text='Км  р:50')

            ],
            [
                KeyboardButton(text='В раздел мужские')
            ],
        ], resize_keyboard=True

    )
    return sport_shoes


def men_boots_size_kb():
    boots = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='См. Смотреть все размеры')
            ], [
                KeyboardButton(text='См  р:39'),
                KeyboardButton(text='См  р:40'),
                KeyboardButton(text='См  р:41'),
                KeyboardButton(text='См  р:42'),
                KeyboardButton(text='См  р:43')

            ], [KeyboardButton(text='См  р:44'),
                KeyboardButton(text='См  р:45'),
                KeyboardButton(text='См  р:46'),
                KeyboardButton(text='См  р:47'),
                KeyboardButton(text='См  р:48')

                ], [
                KeyboardButton(text='В раздел мужские')
            ],
        ], resize_keyboard=True
    )
    return boots


def men_short_boots_size_kb():
    short_boots = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Бм. Смотреть все размеры')
            ], [
                KeyboardButton(text='Бм  р:39'),
                KeyboardButton(text='Бм  р:40'),
                KeyboardButton(text='Бм  р:41'),
                KeyboardButton(text='Бм  р:42'),
                KeyboardButton(text='Бм  р:43')

            ], [KeyboardButton(text='Бм  р:44'),
                KeyboardButton(text='Бм  р:45'),
                KeyboardButton(text='Бм  р:46'),
                KeyboardButton(text='Бм  р:47'),
                KeyboardButton(text='Бм  р:48')

                ], [
                KeyboardButton(text='В раздел мужские')
            ],
        ], resize_keyboard=True
    )
    return short_boots


def men_sabo_size_kb():
    sabo = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Мс. Смотреть все размеры')
            ], [
                KeyboardButton(text='Мс  р:39'),
                KeyboardButton(text='Мс  р:40'),
                KeyboardButton(text='Мс  р:41'),
                KeyboardButton(text='Мс  р:42'),
                KeyboardButton(text='Мс  р:43')

            ], [KeyboardButton(text='Мс  р:44'),
                KeyboardButton(text='Мс  р:45'),
                KeyboardButton(text='Мс  р:46'),
                KeyboardButton(text='Мс  р:47'),
                KeyboardButton(text='Мс  р:48')

                ], [
                KeyboardButton(text='В раздел мужские')
            ],
        ], resize_keyboard=True
    )
    return sabo


def kids_shoes_size_kb():
    shoes = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Тд. Смотреть все размеры')
            ], [
                KeyboardButton(text='Тд  р:21'),
                KeyboardButton(text='Тд  р:22'),
                KeyboardButton(text='Тд  р:23'),
                KeyboardButton(text='Тд  р:24'),
                KeyboardButton(text='Тд  р:25')

            ], [
                KeyboardButton(text='Тд  р:26'),
                KeyboardButton(text='Тд  р:27'),
                KeyboardButton(text='Тд  р:28'),
                KeyboardButton(text='Тд  р:29'),
                KeyboardButton(text='Тд  р:30')

            ], [
                KeyboardButton(text='Тд  р:31'),
                KeyboardButton(text='Тд  р:32'),
                KeyboardButton(text='Тд  р:33'),
                KeyboardButton(text='Тд  р:34'),
                KeyboardButton(text='Тд  р:35')
            ], [
                KeyboardButton(text='Тд  р:36'),
                KeyboardButton(text='Тд  р:37'),
                KeyboardButton(text='Тд  р:38'),
                KeyboardButton(text='Тд  р:39'),
                KeyboardButton(text='Тд  р:40')
            ],
            [
                KeyboardButton(text='В раздел детские')
            ],
        ], resize_keyboard=True
    )
    return shoes


def kids_boots_size_kb():
    boots = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Бд. Смотреть все размеры')
            ], [
                KeyboardButton(text='Бд  р:21'),
                KeyboardButton(text='Бд  р:22'),
                KeyboardButton(text='Бд  р:23'),
                KeyboardButton(text='Бд  р:24'),
                KeyboardButton(text='Бд  р:25')

            ], [
                KeyboardButton(text='Бд  р:26'),
                KeyboardButton(text='Бд  р:27'),
                KeyboardButton(text='Бд  р:28'),
                KeyboardButton(text='Бд  р:29'),
                KeyboardButton(text='Бд  р:30')

            ], [
                KeyboardButton(text='Бд  р:31'),
                KeyboardButton(text='Бд  р:32'),
                KeyboardButton(text='Бд  р:33'),
                KeyboardButton(text='Бд  р:34'),
                KeyboardButton(text='Бд  р:35')
            ], [
                KeyboardButton(text='Бд  р:36'),
                KeyboardButton(text='Бд  р:37'),
                KeyboardButton(text='Бд  р:38'),
                KeyboardButton(text='Бд  р:39'),
                KeyboardButton(text='Бд  р:40')
            ],
            [
                KeyboardButton(text='В раздел детские')
            ],
        ], resize_keyboard=True
    )
    return boots


def women_shoes_kb():
    shoes = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Тж Смотреть все размеры')
            ], [
                KeyboardButton(text='Тж  р:36'),
                KeyboardButton(text='Тж  р:37'),
                KeyboardButton(text='Тж  р:38'),
                KeyboardButton(text='Тж  р:39')
            ], [
                KeyboardButton(text='Тж  р:40'),
                KeyboardButton(text='Тж  р:41'),
                KeyboardButton(text='Тж  р:42'),
                KeyboardButton(text='Тж  р:43')
            ], [
                KeyboardButton(text='В раздел женские')
            ]
        ], resize_keyboard=True
    )
    return shoes


def women_sabo_kb():
    sabo = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Сж Смотреть все размеры')
            ], [
                KeyboardButton(text='Сж  р:36'),
                KeyboardButton(text='Сж  р:37'),
                KeyboardButton(text='Сж  р:38'),
                KeyboardButton(text='Сж  р:39')
            ], [
                KeyboardButton(text='Сж  р:40'),
                KeyboardButton(text='Сж  р:41'),
                KeyboardButton(text='Сж  р:42'),
                KeyboardButton(text='Сж  р:43')
            ], [
                KeyboardButton(text='В раздел женские')
            ]
        ], resize_keyboard=True
    )
    return sabo


def women_boots_kb():
    boot = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Бж Смотреть все размеры')
            ], [
                KeyboardButton(text='Бж  р:36'),
                KeyboardButton(text='Бж  р:37'),
                KeyboardButton(text='Бж  р:38'),
                KeyboardButton(text='Бж  р:39')
            ], [
                KeyboardButton(text='Бж  р:40'),
                KeyboardButton(text='Бж  р:41'),
                KeyboardButton(text='Бж  р:42'),
                KeyboardButton(text='Бж  р:43')
            ], [
                KeyboardButton(text='В раздел женские')
            ]
        ], resize_keyboard=True
    )
    return boot
