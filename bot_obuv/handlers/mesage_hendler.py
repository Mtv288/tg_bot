from aiogram import F, Router
from aiogram.types import Message
from bot_obuv.keyboard.inline_keyboard import select_type_shoes_kb

router = Router()


def answer_for_message(type_shoes):
    answer = f'Если вы хотите посмотреть ассортимент обуви нажмите на кнопку ' \
             f'{type_shoes} внизу экрана и выберите интересующую вас категорию обуви'
    return answer


def search_in_word(message_in_chat, word_1, word_2):
    if word_1 and word_2 in message_in_chat:
        return word_1, word_2


@router.message(lambda message: 'жен' in message.text.lower())
async def woman_shoes(message: Message):
    await message.reply(answer_for_message('"Женская обувь"'))


@router.message(lambda message: 'муж' in message.text.lower())
async def men_shoes(message: Message):
    await message.reply(answer_for_message('"Мужская обувь"'))


@router.message(lambda message: 'дет' in message.text.lower())
async def kid_shoes(message: Message):
    await message.reply(answer_for_message('"Детская обувь"'))


@router.message(lambda message: 'тап' in message.text.lower())
async def slippers(message: Message):
    await message.reply(answer_for_message('"Тапки"'))


@router.message(lambda message: 'работа' in message.text.lower())
async def job_time(message: Message):
    await message.reply('_____Наш режим работы:_____'
                        '  Понедельник - Пятница с 8.00 до 17.30'
                        '  Суббота - Воскресенье с 9.00 до 16.00'
                        '  без перерывов и выходных')


@router.message(F.text == 'Помощь.')
async def slippers(message: Message):
    await message.reply('Это небольшая инструкция как пользоваться помощником в чате')
    await message.reply('Внизу вы видите кнопки с разделами, нажимая на них вы переходите в соответсвующие разделы '
                        'позволяющие выбрать интересующий вас тип обуви и посмотреть фото и цены,'
                        'все фото и цены актуальны показано то что есть в наличии на момент когда вы смотрите')
    await message.reply('Если вас интересует определенная модель обуви, то в поле сообщение наберите '
                        'код модели, например "99-555", код модели находится на фото и выглядит как "ЧЧ-ЧЧЧ"')
    await message.reply('Или можно просто набрать сообщение допустим "мужские летние"')
    await message.delete()


@router.message()
async def price(message: Message):
    mes = ''.join(message.text.lower())
    print(mes)
    for i in ['цен', 'стоит', 'почем']:
        if i in mes:
            await message.reply('Чтобы узнать цену и наличие размеров, '
                            'введите артикул модели который находится на фото и '
                            'выглядит в таком формате "99-999".(Вместо девяток подставьте нужные цифры) ')

@router.message()
async def select_inl(message: Message):

    if message.text == 'Тип':
        await message.reply('Выберите мужские или женские', reply_markup=select_type_shoes_kb)
    else:
        if len(message.text) != 6 and message.text != 'Помощь.':
            await message.reply('Я вас не понял повторите вопрос более корректно')




