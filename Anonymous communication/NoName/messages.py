from database.sqlite_db import sql_return_name, sql_return_notification, sql_return_unread_messages, sql_return_description, sql_interlocutor, sql_return_interlocutor
from aiogram import types
from keyboards.in_kb import in_kb_menu

greeting_mes = "👤 ИМЯ: {0}\n\n💼 О себе: {1}\n\n✉️ Непрочитанные сообщения: {2}\n\n{3} Уведомления {4}"

first_enter_mes = "Чтобы начать работу с ботом для анонимных переписок, придумайте себе имя, которое будет отображаться другим пользователям. Имя можно потом изменить."

about_bot_mes = "@anonimizator_bot - Бот, который создан для анонимного общения.\n\nСобеседник узнает о вас, только то, что вы сами напишете о себе.\nВы можете в любой момент поменять имя, тем самым создав \"новую личность\".\nЧтобы написать человеку, вам нужно знать его ник.\n\nТех. поддержка: ник - M (англ.)"

about_myself = "Напишите что-нибудь о себе, чтобы пользователи могли понять, чем вы можете им помочь.\n\nНапример:\n⚫️ Оказываю интернет услуги.\n⚫️ Предлагаю подработку.\n⚫️ Занимаюсь поиском людей.\n\n"
skip_about_myself = "Напишите /skip, чтобы пропустить этот этап."

user_was_found = "👤 ИМЯ: {0}\n\n💼 О себе: {1}\n\nДобавив пользователя в контакты, вам не придется постоянно искать его по имени. Добавление одностороннее, т.е. он не узнает, что вы его добавили"

chat_start = "Вы вошли в анонимный чат с пользователем.\nЧтобы выйти из чата, напишите /stop"

MESSAGES_SLASH_COMMANDS = {
    "greeting" : greeting_mes,
    "first_enter" : first_enter_mes,
}

MESSAGES_ABOUT_MYSELF = {
    "about_myself" : about_myself,
    "skip_about_myself" : skip_about_myself
}

async def menu_message (message:types.Message, userID):
    name = await sql_return_name(userID)
    description = await sql_return_description(userID)
    user_messages = await sql_return_unread_messages(userID)
    notification_bell = "🔔" if await sql_return_notification(userID) == 1 else "🔕"
    notification = "Вкл." if await sql_return_notification(userID) == 1 else "Выкл."
    #Сброс собеседника при входе в меню
    await sql_interlocutor(0, message.from_user.id)
    #Замена или отправка нового сообщения
    try:
        await message.edit_text(greeting_mes.format(name, description, user_messages, notification_bell, notification), reply_markup=in_kb_menu)
    except:
        await message.answer(greeting_mes.format(name, description, user_messages, notification_bell, notification), reply_markup=in_kb_menu)


    #if replace:
    #    await message.edit_text(greeting_mes.format(name, description, user_messages, notification_bell, notification), reply_markup=in_kb_menu)
    #else:
    #    await message.answer(greeting_mes.format(name, description, user_messages, notification_bell, notification), reply_markup=in_kb_menu)