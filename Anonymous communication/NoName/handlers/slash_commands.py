from aiogram import types, Dispatcher
from messages import MESSAGES_SLASH_COMMANDS, menu_message
from database.sqlite_db import sql_return_name, sql_check_user, sql_add_userID
from keyboards.in_kb import in_kb_set_name

#userID = types.Message.from_user.id

async def start_cmd (message: types.Message):
    if (await sql_check_user(message.from_user.id) is None) or (await sql_return_name(message.from_user.id) is None):
        await sql_add_userID (message.from_user.id)
        await message.answer(MESSAGES_SLASH_COMMANDS["first_enter"], reply_markup=in_kb_set_name)
    else:
        await menu_message(message, message.from_user.id)#, False)


def register_hendlers_change_name(dp : Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start', 'menu'])