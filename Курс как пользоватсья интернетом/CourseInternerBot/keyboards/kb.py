from re import T
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Buttons
b1 = KeyboardButton("Пройти анализ") 
b2 = KeyboardButton("Продолжить путь") 
b3 = KeyboardButton("Начать") 
b4 = KeyboardButton("Перейти к 3 этапу") 
b5 = KeyboardButton("Возрадоваться и продолжить") 
b6 = KeyboardButton("С удовольствием перейти к оплате чека") 


#keyboard init
kb_start_p1 = ReplyKeyboardMarkup(resize_keyboard=True).add(b1)
kb_start_p2 = ReplyKeyboardMarkup(resize_keyboard=True).add(b2)
kb_start_p3 = ReplyKeyboardMarkup(resize_keyboard=True).add(b4)
kb_start_p4 = ReplyKeyboardMarkup(resize_keyboard=True).add(b5)
kb_continue_p2 = ReplyKeyboardMarkup(resize_keyboard=True).add(b3)
kb_to_pay = ReplyKeyboardMarkup(resize_keyboard=True).add(b6)


#add buttons to keyboards


"""
@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)
"""