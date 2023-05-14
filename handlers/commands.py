import aiohttp
from aiogram import types, Dispatcher
from create_bot import dp, bot
from key.buttons import menu_info


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет!', reply_markup=menu_info)


def register_admin(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])