from database.sqlite_db import sql_add_part
from messages import MESSAGES_P3
from aiogram import types, Dispatcher
from create_bot import bot
from keyboards.in_kb import slider_inkb
from aiogram.types import ReplyKeyboardRemove 
from config import slider_count
from handlers.part2 import change_bool_var

#slider_count = 1 is_inputDonat = False

async def start_part3(message: types.Message):
    await sql_add_part(3, username=message.from_user.username)
    print(message.from_user.first_name+" ("+message.from_user.username + "): "+ "part3-slider")

    await message.answer("А теперь с тобой лично свяжется наш Великий Неповторимый Наш Отец и Брат Гениальнейший Паул, но можно и просто Великий Паул", reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id=message.chat.id, text=MESSAGES_P3["part3_text1"].format(message.from_user.first_name), reply_markup=slider_inkb)
    

async def slider_callback_next(callback: types.CallbackQuery):

    global slider_count

    if slider_count < 7:  
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+ "slider-"+str(slider_count))

        slider_count += 1
        if slider_count == 6:
            change_bool_var(True)
            await bot.edit_message_text(chat_id=callback.message.chat.id ,message_id=callback.message.message_id, text=MESSAGES_P3[f'part3_text{slider_count}'])
            slider_count = 1
        else: 
            await bot.edit_message_text(chat_id=callback.message.chat.id ,message_id=callback.message.message_id, text=MESSAGES_P3[f'part3_text{slider_count}'], reply_markup=slider_inkb)
      
        await callback.answer()

    elif slider_count == 7:
        await callback.answer("Дальше ничего нет", show_alert=True)
    

async def slider_callback_prev(callback: types.CallbackQuery):
    global slider_count
    if slider_count > 1:  
        print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+ "slider-"+str(slider_count))
        slider_count -= 1
        if slider_count == 1:                                                                                     
            await bot.edit_message_text(chat_id=callback.message.chat.id ,message_id=callback.message.message_id, text=MESSAGES_P3['part3_text1'].format(callback.from_user.first_name), reply_markup=slider_inkb)
        else:
            await bot.edit_message_text(chat_id=callback.message.chat.id ,message_id=callback.message.message_id, text=MESSAGES_P3[f'part3_text{slider_count}'], reply_markup=slider_inkb)
        await callback.answer()
    elif slider_count == 1:
        await callback.answer("Ты куда? Это первый слайд", show_alert=True)


def register_hendlers_part3(dp : Dispatcher):
    dp.register_message_handler(start_part3, text= "Перейти к 3 этапу")

    dp. register_callback_query_handler(callback=slider_callback_next, text="slider_next_callback")
    dp. register_callback_query_handler(callback=slider_callback_prev, text="slider_prev_callback")
    
