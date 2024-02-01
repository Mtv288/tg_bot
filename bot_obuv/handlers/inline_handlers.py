from aiogram import F, Router
from aiogram.types.callback_query import CallbackQuery
from aiogram.types import Message, InputFile, InputMediaPhoto, FSInputFile
from bot_obuv.keyboard.inline_keyboard import select_type_shoes_kb
from bot_obuv.keyboard.reply_keyboard import main_kb

router = Router()

photo_for = 'photo_phasad.jpg'


@router.message()
async def search_type_shoes(message: Message):
    list_word_address = ['как', 'ехать', 'где', 'найти']
    for i in list_word_address:
        if i in message.text:
            await message.reply('Если вы хотите узнать наш адрес и контакты '
                                'нажмите кнопку под сообщением', reply_markup=select_type_shoes_kb)
            await message.answer('Главое меню', reply_markup=main_kb())
            break


@router.callback_query()
async def g(callback: CallbackQuery):
    if callback.data == 'адрес':
        await callback.message.reply_photo(photo=FSInputFile('photo_phasad.jpg'),
                                           caption='Наш адрес ул.Привокзальная 17б')
    elif callback.data == 'телефон':
        await callback.message.reply('Наши телефоны:  сот.: +7 928-394-27-63 '
                                     'город.: (8878) 2  21-09-44'
                                     '          WhatsApp: +7 928-394-27-63')
