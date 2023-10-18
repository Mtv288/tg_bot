from aiogram import types


async def start(message: types.Message):
    await message.answer(f'Здравствуйте {message.from_user.first_name}.')
    await message.answer('Я могу показать наличие моделей, их цену а также размеры которые есть на данный момент')
