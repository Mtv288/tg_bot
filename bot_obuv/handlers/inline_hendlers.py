from aiogram import F, Router
from aiogram.types import Message, InputFile, input_media
from sqlalchemy.orm import Session
from bot_obuv.data_base.data_base_main import Catalog
from bot_obuv.data_base.data_base_main import engine
from aiogram import types
from bot_obuv.keyboard.reply_keyboard import main_kb, men_kb, women_kb, \
    slipper_kb, return_kb_men, child_kb, return_kb_women, return_kb_children, return_kb_slippers
from bot_obuv.data_base.data_base_main import list_name_goods, get_price_and_size_good_and_photo

import traceback

router = Router()

