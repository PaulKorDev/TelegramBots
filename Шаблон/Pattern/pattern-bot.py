from aiogram.utils import executor
from create_bot import dp, bot#, storage
from database.sqlite_db import sql_start
from handlers import pattern_handler
from config import URL_APP, PORT

#information for cmd
async def on_startup(_):
    #for webhook
    # await bot.set_webhook(URL_APP)
    print("Bot is running")
    sql_start()

async def on_shutdown(dp):
    #for webhook
    #await bot.delete_webhook()
    await bot.close()
    print("Bot is closed")
    #Если усть fsm
    #await storage.close()
    #print("Storage is closed")

pattern_handler.register_hendlers_pattern(dp)

if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp, 
        skip_updates=True, 
        on_startup=on_startup, 
        on_shutdown=on_shutdown)

"""
executor.start_webhook(
    dispatcher=dp, 
    webhook_path='',
    on_startup=on_startup, 
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=PORT)
"""