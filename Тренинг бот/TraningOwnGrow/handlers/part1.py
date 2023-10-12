from database.sqlite_db import sql_add_part, sql_add_username
from messages import MESSAGES_P1, MESSAGES_START_END
from keyboards.kb import kb_start_p1, kb_start_p2
from keyboards.in_kb import circle_inkb, family_inkb, list_inkb, dog_inkb, baby_inkb, train_inkb
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
        await callback.answer("У тебя правда встает на круги?", show_alert=True)
        print(callback.message.from_user.first_name+" (" + callback.message.from_user.username + "): "+"1-cirle"+"-Возбуждение")
    elif callback.data.endswith("2"):
        await callback.answer("Твоя мать носит очки?", show_alert=True)
        print(callback.message.from_user.first_name+" (" + callback.message.from_user.username + "): "+"1-cirle"+"-Мать")
    elif callback.data.endswith("3"):
        await callback.answer("Серьезно?", show_alert=True)
        print(callback.message.from_user.first_name+" (" + callback.message.from_user.username + "): "+"1-cirle"+"-Колеса")

    await bot.send_photo(callback.from_user.id, IMG['family'], reply_markup=family_inkb)


async def family_inkb_f (callback : types.CallbackQuery):
    if callback.data.endswith("1"):
        await callback.answer("Вам нельзя заводить семью", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"2-family" + " Сжечь")
    elif callback.data.endswith("2"):
        await callback.answer("1хBet", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"2-family" + " Рекалама")
    elif callback.data.endswith("3"):
        await callback.answer("Похоже у вас какие-то проблемы", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"2-family" + " Страх")

    await bot.send_photo(callback.from_user.id, IMG['list'], reply_markup=list_inkb)


async def list_inkb_f (callback : types.CallbackQuery):
    if callback.data.endswith("1"):
        await callback.answer("Марихуана- это не зло, а способ раскрыть сознание", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"3-list"+" Марихуана")
    elif callback.data.endswith("2"):
        await callback.answer("Как тут можно это увидеть?", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"3-list"+" Пол губы")
    elif callback.data.endswith("3"):
        await callback.answer("Вы застряли в 90ых", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"3-list"+" лесополоса")
    await bot.send_photo(callback.from_user.id, IMG['dog'], reply_markup=dog_inkb)


async def dog_inkb_f (callback : types.CallbackQuery):
    if callback.data.endswith("1"):
        await callback.answer("Вы понимаете, что это не нормально?", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"4-dog"+" Моча")
    elif callback.data.endswith("2"):
        await callback.answer("Вы озабоченый", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"4-dog"+" Любовница")
    elif callback.data.endswith("3"):
        await callback.answer("Вы понимаете, что это не нормально?", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"4-dog"+" Утопить")
    await bot.send_photo(callback.from_user.id, IMG['baby'], reply_markup=baby_inkb)


async def baby_inkb_f (callback : types.CallbackQuery):
    if callback.data.endswith("1"):
        await callback.answer("Вы адекватный?", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"5-baby"+" Похищение")
    elif callback.data.endswith("2"):
        await callback.answer("Это же ребенок", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"5-baby"+" эрекция")
    elif callback.data.endswith("3"):
        await callback.answer("Это безответственно", show_alert=True)
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"5-baby"+" хлеб")
    await bot.send_photo(callback.from_user.id, IMG['train'], reply_markup=train_inkb)


async def train_inkb_f (callback : types.CallbackQuery):
    if callback.data.endswith("1"):
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"6-train"+" безнадежность")
    elif callback.data.endswith("2"):
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"6-train"+" шлюха")
    elif callback.data.endswith("3"):
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+"6-train"+" анал")

    await callback.answer("Как вы уже поняли, без помощи тут не обойтись. Хорошо, что вы пришли к нам, ведь мы вам нужны", show_alert=True)
    await callback.message.answer(MESSAGES_P1['part1_text_complete'], reply_markup=kb_start_p2)

def register_hendlers_part1(dp : Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start', 'help'])
    dp.register_message_handler(start_test1, text="Пройти анализ")

    dp.register_callback_query_handler(circle_inkb_f, lambda x: x.data and x.data.startswith('circle_callback'))
    dp.register_callback_query_handler(family_inkb_f, lambda x: x.data and x.data.startswith('family_callback'))
    dp.register_callback_query_handler(list_inkb_f, lambda x: x.data and x.data.startswith('list_callback'))
    dp.register_callback_query_handler(dog_inkb_f, lambda x: x.data and x.data.startswith('dog_callback'))
    dp.register_callback_query_handler(baby_inkb_f, lambda x: x.data and x.data.startswith('baby_callback'))
    dp.register_callback_query_handler(train_inkb_f, lambda x: x.data and x.data.startswith('train_callback'))
 
    