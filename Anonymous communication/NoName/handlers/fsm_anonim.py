#from os import stat
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import Dispatcher, types
from create_bot import dp, bot
from database.sqlite_db import sql_nickname, sql_search_person, sql_return_name, sql_description, sql_return_description, sql_interlocutor, sql_return_interlocutor, sql_return_notification, sql_increment_unread_messages, sql_check_friend, sql_return_dict_mes, sql_dict_mes, sql_decrease_unread_messages
from keyboards.in_kb import in_kb_set_description, create_in_kb_profile
from handlers.slash_commands import start_cmd
from messages import menu_message, MESSAGES_ABOUT_MYSELF, user_was_found, chat_start
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""
    Изменение и установка имени
"""
class FSMNickname (StatesGroup):
    name = State()

async def start_fsm_nickname (callback: types.CallbackQuery):
    await callback.message.edit_text("Имя должно быть не более 20 символов, можете использовать любые символы")
    await FSMNickname.name.set()
    print ("FSM Nickname is running for " + str(callback.from_user.id))

async def name_set_fsm (callback: types.CallbackQuery):
    state = dp.current_state(chat=callback.chat.id, user=callback.from_user.id)

    entered_name = callback.text
    if len(entered_name) > 20:
        await callback.answer("Имя больше 20 символов")
    elif await sql_search_person(entered_name):
        await callback.answer("Это имя занято другим пользователем")
    else:
        if await sql_return_name(callback.from_user.id) is None:    
            await sql_nickname(callback.text, callback.from_user.id)
            await callback.answer("Установленно имя: " + callback.text, reply_markup=in_kb_set_description)
        else:
            await sql_nickname(callback.text, callback.from_user.id)
            await menu_message(callback, callback.from_user.id)#false
        await state.finish()
        print ("FSM Nickname is finishing for " + str(callback.from_user.id))

"""
    Изменение и установка описания
"""
class FSMDescription (StatesGroup):
    description = State()

async def start_fsm_description (callback: types.CallbackQuery):
    await callback.message.edit_text(MESSAGES_ABOUT_MYSELF["about_myself"])
    await callback.message.answer(MESSAGES_ABOUT_MYSELF["skip_about_myself"])
    await FSMDescription.description.set()
    print ("FSM Description is running for " + str(callback.from_user.id))

async def finish_description_fsm (message: types.Message):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    current_state = await state.get_state()
    if current_state is None:
        return
    await menu_message(message, message.from_user.id)#false
    await state.finish()
    print ("FSM Description is finishing for " + str(message.from_user.id))

async def description_set_fsm (callback: types.CallbackQuery):
    state = dp.current_state(chat=callback.chat.id, user=callback.from_user.id)

    entered_desc = callback.text
    if len(entered_desc) > 255:
        await callback.answer("Описание больше 255 символов")
    else:
        await sql_description(callback.text, callback.from_user.id)
        await start_cmd(callback)
        await state.finish()
        print ("FSM Description is finishing for " + str(callback.from_user.id))

"""
    Вызов "профиля"
"""
async def return_profile (message: types.Message, name, id_other_user):
    try:
        await message.edit_text(user_was_found.format(name, await sql_return_description(id_other_user)), reply_markup=create_in_kb_profile(id_other_user, await sql_check_friend(id_other_user, message.chat.id) is None))
    except Exception as exc:
        print(f"except: {exc}")
        await message.answer(user_was_found.format(name, await sql_return_description(id_other_user)), reply_markup=create_in_kb_profile(id_other_user, await sql_check_friend(id_other_user, message.chat.id) is None))
    
"""
    Поиск человека по имени
"""
class FSMFindName (StatesGroup):
    search = State()

async def start_fsm_findname (callback: types.CallbackQuery):
    await callback.message.edit_text("Введите имя пользователя, которого вы ищете")
    await callback.message.answer("Команда /menu вернет вас в главное меню")
    await FSMFindName.search.set()
    print ("FSM FindName is running for " + str(callback.from_user.id))

async def finish_search_name_fsm(message: types.Message):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await menu_message(message, message.from_user.id)#False
    print ("FSM FindName is finishing for " + str(message.from_user.id) + " user was not found")

async def search_name_fsm (message: types.Message):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

    entered_name = message.text
    id_other_user = await sql_search_person(entered_name)
    if len(entered_name) > 20:
        await message.answer("Имя больше 20 символов")
    elif id_other_user is None:
        await message.answer("Пользователь не найден, возможно вы неправильно ввели имя, либо он изменил свой ник")
    elif entered_name == await sql_return_name(message.from_user.id):
        await message.answer("Да, это вы")
    elif id_other_user:
        await message.answer("Пользователь найден!\n\n")
        await return_profile(message, entered_name, id_other_user)
        await state.finish()
        print("FSM FindName is finishing for " + str(message.from_user.id))
        #await sql_interlocutor(id_other_user, message.from_user.id)

"""
    ЧАТ
"""

class FSMChat (StatesGroup):
    chat = State()

async def start_fsm_chat (callback: types.CallbackQuery):
    state = dp.current_state(chat=callback.message.chat.id, user=callback.from_user.id)
    interlocutor = callback.data.replace('_write_callback', '')
    if await state.get_state() is None: 
        if callback.data and callback.data.endswith('_write_callback'):   
            await sql_interlocutor(interlocutor, callback.from_user.id)
    
        try:
            await callback.message.edit_text(chat_start)
        except:
            await callback.answer(chat_start)
        await FSMChat.chat.set()
        print ("FSM Chat is running for " + str(callback.from_user.id))
        
        #ВЫВОД НЕПРОЧИТАННЫХ СООБЩЕНИЙ
        dict_mes = await sql_return_dict_mes(callback.from_user.id)
        if (dict_mes is None) or (interlocutor not in dict_mes):
            pass
        else:
            await callback.message.answer(f"Непрочитанные сообщение от {await sql_return_name(interlocutor)}:")
            for mes in dict_mes[f'{interlocutor}']:
                if mes.endswith("_PHOTO"):
                    await bot.send_photo(callback.message.chat.id, photo=mes.replace("_PHOTO",""))
                else:    
                    await callback.message.answer(mes)
                await sql_decrease_unread_messages(callback.from_user.id)
            del dict_mes[f'{interlocutor}']
            await sql_dict_mes(dict_mes, callback.from_user.id)

    else:
        await callback.answer("Вы сейчас не можете войти в чат, завершите все процессы")
        
async def finish_chat_fsm(message: types.Message):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)   
    if await state.get_state() is None:
        return    
    await state.finish()
    await menu_message(message, message.from_user.id)#False
    print ("FSM Chat is finishing for " + str(message.from_user.id))

async def process_chat_fsm_mes (message: types.Message):
    photo = 0
    if message == types.ContentTypes.PHOTO:
        photo = message.photo[-1].file_id

    interlocutor = await sql_return_interlocutor(message.from_user.id)
    #Отправка собеседнику
    #сделать тут отправку фото
    if (await sql_return_interlocutor(interlocutor)==message.from_user.id):
        if photo:
            await bot.send_photo(chat_id=interlocutor, caption="Фотография от {0}:\n{1}\n".format(await sql_return_name(message.from_user.id), photo=photo))
        else:
            await bot.send_message(chat_id=interlocutor, text="Сообщение от {0}:\n{1}\n".format(await sql_return_name(message.from_user.id), message.text))
    else:
        if await sql_return_notification(interlocutor):
            await bot.send_message(chat_id=interlocutor, text="Вам сообщение от {0}".format(await sql_return_name(message.from_user.id)), reply_markup=InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="Перейти в чат", callback_data=f"{message.from_user.id}_write_callback")))
        await sql_increment_unread_messages(interlocutor)
    # Отправка отправителю
        await bot.send_message(chat_id=message.from_user.id, text="Отправленно {0}:\n{1}\n\n".format(await sql_return_name(interlocutor), message.text))#, reply_markup=in_kb_message_menu)
    #занесение сообщения в словарь    
        dict_mes = await sql_return_dict_mes(interlocutor)
        mes = f"{photo}_PHOTO" if photo else message.text
        if dict_mes is None:
            dict_mes = {f'{message.from_user.id}': [mes]}
        elif str(message.from_user.id) not in dict_mes:
            dict_mes.update({f'{message.from_user.id}': [mes]})
        else:
            dict_mes[f'{message.from_user.id}'] = dict_mes[f'{message.from_user.id}'] + [mes]
        #занесение в бд
        await sql_dict_mes(dict_mes, interlocutor)

def register_handlers_fsm(dp: Dispatcher):
    #установить или изменить имя
    dp.register_callback_query_handler(start_fsm_nickname, text="set_name_callback", state=None)
    dp.register_message_handler(name_set_fsm, state=FSMNickname.name)
    #установить или изменить описание
    dp.register_callback_query_handler(start_fsm_description, text="set_description_callback", state=None)
    dp.register_message_handler(finish_description_fsm, commands=["skip", "menu", "start"], state=FSMDescription.description)
    dp.register_message_handler(description_set_fsm, state=FSMDescription.description)
    #поиск человека по имени
    dp.register_callback_query_handler(start_fsm_findname, text="find_user_callback", state=None)
    dp.register_message_handler(finish_search_name_fsm, commands=["menu", "start"], state=FSMFindName.search)
    dp.register_message_handler(search_name_fsm, state=FSMFindName.search)
    #чат
    dp.register_callback_query_handler(start_fsm_chat, lambda x: x.data and x.data.endswith('_write_callback'), state="*")
    dp.register_callback_query_handler(start_fsm_chat, lambda x: x.data and x.data.endswith('_reply_callback'), state="*")
    dp.register_message_handler(finish_chat_fsm, commands=["stop", "menu", "start"], state=FSMChat.chat)
    dp.register_message_handler(process_chat_fsm_mes, state=FSMChat.chat, content_types=types.ContentTypes.PHOTO)
    dp.register_message_handler(process_chat_fsm_mes, state=FSMChat.chat)
    #dp.register_message_handler(state="*") - Ловит все состояния


#Сохранение данных (ПРИМЕР):
#data = await state.get_data()
#answer1 = data.get("answer1")
    
#Удобно если нужно:
#data["some_digit"] += 1
#data["some_list"].append(1)


#Тоже самое что и:

#data = await state.get_data()
#some_list = data.get("some_list")
#some_list.append(1)
#await state.update_data(some_list=some_list)
