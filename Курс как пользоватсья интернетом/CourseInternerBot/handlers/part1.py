from database.sqlite_db import sql_add_part, sql_add_username
from messages import MESSAGES_P1, MESSAGES_START_END
from keyboards.kb import kb_start_p1, kb_start_p2
from keyboards.in_kb import circle_inkb, family_inkb
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove 
from create_bot import bot#, dp
from config import IMG


async def start_cmd(message: types.Message):
    await message.answer(MESSAGES_START_END['title_text'])
    await message.answer(MESSAGES_START_END['introduce_text'], reply_markup=kb_start_p1)
    print(message.from_user.first_name+" ("+message.from_user.username + "): "+"start")

    try:
        await sql_add_username(message.from_user.username)
    except Exception as e:
        print("sql_add_username:\n" + e)
    await sql_add_part(1, message.from_user.username)
    print(message.from_user.first_name+" ("+message.from_user.username + "): "+"part1-picAssotiation")

async def start_test1(message: types.Message):
    await message.answer(MESSAGES_P1['part1_text'], reply_markup=ReplyKeyboardRemove())
    await bot.send_photo(message.from_user.id, IMG['circles'], reply_markup=circle_inkb)


async def circle_inkb_f (callback : types.CallbackQuery):
    if callback.data.endswith("1"):
        await callback.answer("Тут нет кругов", show_alert=True)
        print(callback.message.from_user.first_name+" (" + callback.message.from_user.username + "): "+"1-cirle"+"-Круг")
    elif callback.data.endswith("2"):
        await callback.answer("Тут нет зеленого", show_alert=True)
        print(callback.message.from_user.first_name+" (" + callback.message.from_user.username + "): "+"1-cirle"+"-Зеленый")
    elif callback.data.endswith("3"):
        await callback.answer("Их три", show_alert=True)
        print(callback.message.from_user.first_name+" (" + callback.message.from_user.username + "): "+"1-cirle"+"-Три")

    await bot.send_photo(callback.from_user.id, IMG['family'], reply_markup=family_inkb)


async def family_inkb_f (callback : types.CallbackQuery):
    if callback.data.endswith("1"):
        await callback.answer("Нет, стирка", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"2-family" + " Новый год")
    elif callback.data.endswith("2"):
        await callback.answer("Маленькие собачки", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"2-family" + " Котята")
    elif callback.data.endswith("3"):
        await callback.answer("Нельзя правильно отвечать", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"2-family" + " Щенки в носках")

    await callback.answer("Как вы уже поняли, без помощи тут не обойтись. Хорошо, что вы пришли к нам, ведь мы вам нужны", show_alert=True)
    await callback.message.answer(MESSAGES_P1['part1_text_complete'], reply_markup=kb_start_p2)

def register_hendlers_part1(dp : Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start', 'help'])
    dp.register_message_handler(start_test1, text="Пройти анализ")

    dp.register_callback_query_handler(circle_inkb_f, lambda x: x.data and x.data.startswith('circle_callback'))
    dp.register_callback_query_handler(family_inkb_f, lambda x: x.data and x.data.startswith('family_callback'))

 
    