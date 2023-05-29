import aiohttp
from aiogram import types, Dispatcher

from config import AUTHORIZED_USER_ID
from create_bot import dp, bot
from key.buttons import menu_info


async def start(message: types.Message):
    if str(message.from_user.id) in AUTHORIZED_USER_ID:
        await bot.send_message(message.from_user.id, 'Привет!', reply_markup=menu_info)
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Sorry, you are not authorized to use this bot.")


def register_admin(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])