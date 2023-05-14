from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton

b1 = KeyboardButton('Файл')

menu_info = ReplyKeyboardMarkup(resize_keyboard=True)
menu_info.add(b1)