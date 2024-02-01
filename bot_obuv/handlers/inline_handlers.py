from aiogram import Router
from aiogram.types.callback_query import CallbackQuery
from aiogram.types import Message, FSInputFile
from bot_obuv.keyboard.inline_keyboard import select_type_shoes_kb
from bot_obuv.keyboard.reply_keyboard import main_kb

router = Router()


@router.message()
async def search_type_shoes(message: Message):
    list_word_address = ['как', 'ехать', 'где', 'найти']
    for i in list_word_address:
        if i in message.text.lower():
            await message.reply('Если вы хотите узнать наш адрес и контакты '
                                'нажмите нужную кнопку под сообщением', reply_markup=select_type_shoes_kb)
            await message.answer('Главое меню', reply_markup=main_kb())
            break


@router.callback_query()
async def g(callback: CallbackQuery):
    if callback.data == 'адрес':
        await callback.message.reply_photo(photo=FSInputFile('facade.jpg'),
                                           caption='Наш адрес ул.Привокзальная 17.Б')
    elif callback.data == 'телефон':
        await callback.message.reply('Наши телефоны:  сот.: +7 928-394-27-63 '
                                     'город.: (8878) 2  21-09-44'
                                     '          WhatsApp: +7 928-394-27-63')
