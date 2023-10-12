from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.sqlite_db import sql_return_name, sql_return_dict_mes

#Buttons
my_mess_but = InlineKeyboardButton(text=f"📪 Мои сообщения", callback_data="my_mess_callback")
find_user_but = InlineKeyboardButton(text="🔎 Поиск по имени", callback_data="find_user_callback")
friend_list = InlineKeyboardButton(text="👤 Добавленные контакты", callback_data="friend_list_callback")
notification_but = InlineKeyboardButton(text="🔔 Выкл/Вкл уведомления", callback_data="notification_callback")
change_name_but = InlineKeyboardButton(text="🎭 Изменить имя", callback_data="set_name_callback")
change_descroption_but = InlineKeyboardButton(text="✏️ Написать о себе", callback_data="set_description_callback")
about_bot_but  = InlineKeyboardButton(text="🤖 О боте", callback_data="about_bot_callback")

set_name_but = InlineKeyboardButton(text="Придумать имя", callback_data="set_name_callback")
set_description_but = InlineKeyboardButton(text="Продолжить", callback_data="set_description_callback")

back_but = InlineKeyboardButton(text="Назад", callback_data="back_callback")

tech_support_but = InlineKeyboardButton(text="Создатель бота", callback_data="5332747174_profile_callback")

write_but = InlineKeyboardButton(text="💬Написать💬", callback_data="_write_callback")
friend_but = InlineKeyboardButton(text="❇️ Добавить в быстрые контакты ❇️", callback_data="_friend_callback")

#keyboard init
in_kb_menu = InlineKeyboardMarkup(row_width=1)
in_kb_set_name = InlineKeyboardMarkup(row_width=1)
in_kb_about_bot = InlineKeyboardMarkup(row_width=1)
in_kb_set_description = InlineKeyboardMarkup(row_width=1)
in_kb_person_found = InlineKeyboardMarkup(row_width=1)

#add buttons to keyboards
in_kb_menu.add(my_mess_but).add(find_user_but).add(friend_list).add(notification_but).add(change_name_but).add(change_descroption_but).add(about_bot_but)
in_kb_set_name.add(set_name_but)
in_kb_set_description.add(set_description_but)
in_kb_about_bot.add(tech_support_but).add(back_but)
in_kb_person_found.add(write_but).add(friend_but).add(back_but)


def create_in_kb_profile (id_other_user, add_friend_chek):
    write_but.callback_data = f"{id_other_user}_write_callback"
    if add_friend_chek:       
        friend_but.text = "❇️ Добавить в быстрые контакты ❇️"
        friend_but.callback_data = f"{id_other_user}_add_friend_callback"       
    else:
         
        friend_but.text = "❌ Удалить из быстрых контактов ❌"
        friend_but.callback_data = f"{id_other_user}_delete_friend_callback"  
    return in_kb_person_found

async def create_in_kb_friendlist (friendlist, id_user):
        
    in_kb_friendlist = InlineKeyboardMarkup(row_width=1)
    dict_mes = await sql_return_dict_mes(id_user)
    if friendlist is None:
        in_kb_friendlist.add(InlineKeyboardButton(text=f"Ваш список пуст", callback_data="back_callback"))
    elif type(friendlist) is list:
        for id_friend in friendlist:
            in_kb_friendlist.add(InlineKeyboardButton(text=f"{await sql_return_name(id_friend)}", callback_data=f"{id_friend}_profile_callback"))
    elif type(friendlist) is str:
        in_kb_friendlist.add(InlineKeyboardButton(text=f"{await sql_return_name(friendlist)} ", callback_data=f"{friendlist}_profile_callback"))
    in_kb_friendlist.add(back_but)
    return in_kb_friendlist

async def create_in_kb_unread_mes (id_user):
    in_kb_unread_messages = InlineKeyboardMarkup(row_width=1)
    dict_mes = await sql_return_dict_mes(id_user)
    if (dict_mes is None) or (dict_mes == {}):
        in_kb_unread_messages.add(InlineKeyboardButton(text=f"У вас нет непрочитанных сообщений", callback_data="back_callback"))
    else:
        for id_sender in dict_mes:
            in_kb_unread_messages.add(InlineKeyboardButton(text=f"{await sql_return_name(id_sender)} [{len(dict_mes[str(id_sender)])}]", callback_data=f"{id_sender}_write_callback"))
    in_kb_unread_messages.add(back_but)
    return in_kb_unread_messages


#Full string
#InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="", callback_data="_callback"))
