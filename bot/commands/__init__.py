__all__ = ['register_user_command']

from aiogram import Router

from bot.commands.start import start
from aiogram.filters.command import Command


def register_user_command(router: Router) -> None:
    router.message.register(start, Command(commands=['start']))
