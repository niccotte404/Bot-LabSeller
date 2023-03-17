from aiogram import types, Dispatcher
from database import db
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import os


async def func(message: types.Message):
    pass


def reg_handlers(dp):
    dp.register_message_handler(func)