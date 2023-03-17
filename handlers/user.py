from aiogram import types, Dispatcher
from database import db


async def func(message: types.Message):
    pass


def reg_handlers(dp):
    dp.register_message_handler(func)