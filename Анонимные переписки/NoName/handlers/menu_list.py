from aiogram import types, Dispatcher
from database.sqlite_db import sql_return_notification, sql_notification, sql_friends, sql_return_name, sql_delete_friends, sql_return_friends
from handlers.slash_commands import menu_message
from keyboards.in_kb import in_kb_about_bot, create_in_kb_friendlist, create_in_kb_unread_mes
#from keyboards.kb import kb_person_not_found
from messages import about_bot_mes
from handlers.fsm_anonim import return_profile


async def change_notification (callback: types.CallbackQuery):
    if (await sql_return_notification(callback.from_user.id) == 1):
        await sql_notification(False,callback.from_user.id)
    else:
        await sql_notification(True,callback.from_user.id)
    await menu_message(callback.message, callback.from_user.id)

async def about_bot (callback: types.CallbackQuery):
    await callback.message.edit_text(text=about_bot_mes, reply_markup=in_kb_about_bot)

#async def find_user (callback: types.CallbackQuery):
#    await callback.message.edit_text("Введите имя человека, которого вы ищете",reply_markup=kb_person_not_found)

async def back_cmd (callback: types.CallbackQuery):
    await menu_message(callback.message, callback.from_user.id)

async def friend_add_delete (callback: types.CallbackQuery):
    interlocutor = callback.data.split('_')[0]
    id_user = callback.from_user.id
    if callback.data.endswith('_add_friend_callback'):
        await sql_friends(interlocutor, id_user)
    elif callback.data.endswith('_delete_friend_callback'):
        await sql_delete_friends(interlocutor, id_user)
    await return_profile(callback.message, await sql_return_name(interlocutor), interlocutor) 

async def show_friendlist (callback: types.CallbackQuery):
    try:
        await callback.message.edit_text("Список быстрых контактов:", reply_markup=await create_in_kb_friendlist(await sql_return_friends(callback.from_user.id), callback.from_user.id))
    except:
        await callback.message.answer("Список быстрых контактов:", reply_markup=await create_in_kb_friendlist(await sql_return_friends(callback.from_user.id), callback.from_user.id))

async def show_profile(callback: types.CallbackQuery):
    id_other_user = callback.data.replace('_profile_callback', '')
    name = await sql_return_name(id_other_user)
    await return_profile(callback.message, name, id_other_user)

async def show_unread_messages (callback: types.CallbackQuery):
    try:
        await callback.message.edit_text("Ваши непрочитанные сообщения:", reply_markup=await create_in_kb_unread_mes(callback.from_user.id))
    except:
        await callback.message.answer("Ваши непрочитанные сообщения:", reply_markup=await create_in_kb_unread_mes(callback.from_user.id))

def register_hendlers_menu(dp : Dispatcher):
    dp.register_callback_query_handler(change_notification, text="notification_callback")
    dp.register_callback_query_handler(about_bot, text="about_bot_callback")
    dp.register_callback_query_handler(friend_add_delete, lambda x: x.data and (x.data.endswith('_add_friend_callback') or x.data.endswith('_delete_friend_callback')))
    dp.register_callback_query_handler(back_cmd, text="back_callback")
    dp.register_callback_query_handler(show_friendlist, text="friend_list_callback")
    dp.register_callback_query_handler(show_profile, lambda x: x.data and x.data.endswith('_profile_callback'))
    dp.register_callback_query_handler(show_unread_messages, text="my_mess_callback")

