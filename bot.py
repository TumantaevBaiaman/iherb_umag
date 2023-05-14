

from create_bot import dp
from aiogram.utils import executor
from handlers import admin, commands

commands.register_admin(dp)
admin.register_admin(dp)
executor.start_polling(dp, skip_updates=True)