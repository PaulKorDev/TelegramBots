from aiogram.utils import executor
from create_bot import dp
from database.sqlite_db import sql_start
from handlers import part1, part2, part3, part4

#information for cmd
async def on_startup(_):
    print("Bot is running")
    sql_start()

#Handlers register
part1.register_hendlers_part1(dp)
part2.register_hendlers_part2(dp)
part3.register_hendlers_part3(dp)
part4.register_hendlers_part4(dp)
part2.register_hendlers_part2_empty_handler(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)