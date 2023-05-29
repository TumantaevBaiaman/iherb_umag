import asyncio

from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import AUTHORIZED_USER_ID
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from key.buttons import menu_info
from main import write_to_file


class FSMAdmin(StatesGroup):
    file = State()
    name = State()
    text = State()
    sum = State()


async def cm_start(message: types.Message):
    if str(message.from_user.id) in AUTHORIZED_USER_ID:
        await bot.send_message(message.from_user.id, 'Загрузите файл')
        await FSMAdmin.file.set()
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Sorry, you are not authorized to use this bot.")


async def load_file(message: types.Message, state: FSMAdmin):

    file_info = await bot.get_file(message.document.file_id)
    file_path = file_info.file_path

    file_name = "test.xlsx"
    with open(file_name, "wb") as f:
        file = await bot.download_file(file_path)
        f.write(file.read())

    await bot.send_message(message.from_user.id, f"Файл был успешно загружен. Немного подождите.")
    await state.finish()

    write_to_file()
    with open("Поступление.xlsx", 'rb') as file:
        await bot.send_document(message.from_user.id, file, caption="Поступление.xlsx")


def register_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, Text(equals='Файл', ignore_case=True))
    dp.register_message_handler(load_file, content_types=['document'], state=FSMAdmin.file)