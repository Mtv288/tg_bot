from aiogram import Router, Bot
from aiogram.types import CallbackQuery

router = Router()
@router.callback_query
async def cal(call):
    answer = ('ПРивет пля')
    await call.message.answer(answer)

cal(cal)



