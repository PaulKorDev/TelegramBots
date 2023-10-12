from aiogram.utils import executor
from create_bot import dp, storage, bot
from database import sqlite_db
from handlers import fsm_anonim, menu_list, slash_commands
from database.sqlite_db import sql_return_friends

#information for cmd
async def on_startup(_):
    print("Bot is running")
    sqlite_db.sql_start()

async def on_shutdown(dp):
    await bot.close()
    print("Bot is closed")
    await storage.close()
    print("Storage is closed")

slash_commands.register_hendlers_change_name(dp)
fsm_anonim.register_handlers_fsm(dp)
menu_list.register_hendlers_menu(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)