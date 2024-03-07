from aiogram import Router
from aiogram.types.callback_query import CallbackQuery
from aiogram.types import Message, FSInputFile
import asyncio

router = Router()


@router.callback_query()
async def g(callback: CallbackQuery):
    if callback.data == 'адрес':
        rep = await callback.message.reply_photo(photo=FSInputFile('facade.jpg'),
                                                 caption='Наш адрес ул.Привокзальная 17.Б, Если хотите найти нас на карте нажмите '
                                                         'на эту ссылку: '
                                                         ' https://yandex.ru/maps/1104/cherkessk'
                                                         '/house/privokzalnaya_ulitsa_17b/YEsYdgFmQUwFQFpufX5yeX5hYA==/?ll=42.066'
                                                         '784%2C44.237630&z=17.49')
        await callback.answer()

        await asyncio.sleep(25)
        if rep:
            await rep.delete()

    elif callback.data == 'телефон':
        rep = await callback.message.reply('Наши телефоны: сот.: +7 928-394-27-63 '
                                           '   город.: (8878) 2  21-09-44'
                                           '   WhatsApp: +7 928-394-27-63')
        await callback.answer()
        await asyncio.sleep(25)
        if rep:
            await rep.delete()
    await update_user_visits(message.from_user.full_name, message.from_user.id)
