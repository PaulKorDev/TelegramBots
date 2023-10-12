from messages import MESSAGES_P2, MESSAGES_P3
from aiogram import types, Dispatcher
from keyboards.kb import kb_continue_p2, kb_start_p3, kb_start_p4
from aiogram.types import ReplyKeyboardRemove
from create_bot import bot
from database.sqlite_db import sql_add_donat, sql_add_part, sql_return_donat
from config import count_mess, is_inputDonat
#from handlers.part3 import is_inputDonat, slider_count

def change_bool_var (bool_var):
    global is_inputDonat
    is_inputDonat = bool_var

async def start_part2(message: types.Message):
    await message.answer(MESSAGES_P2["part2_text1"])
    await message.answer(MESSAGES_P2["part2_text2"], reply_markup=kb_continue_p2)
    await sql_add_part(2, message.from_user.username)
    print(message.from_user.first_name+" ("+message.from_user.username + "): "+"part2-zagadka")



async def next_part2(message: types.Message):
    await message.answer(MESSAGES_P2["part2_text3"], reply_markup=ReplyKeyboardRemove())
    global count_mess
    count_mess = 1

async def chek_text_answer(message: types.Message):
    
    global count_mess, is_inputDonat

    if count_mess == 1:
        print(message.from_user.first_name+" ("+message.from_user.username + "): "+ message.text)
        await message.reply(MESSAGES_P2["part2_text_try1"])
        count_mess += 1

    elif count_mess == 2:
        print(message.from_user.first_name+" ("+message.from_user.username + "): "+ message.text)
        await message.reply(MESSAGES_P2["part2_text_try2"])

        count_mess += 1
    elif count_mess == 3:
        print(message.from_user.first_name+" ("+message.from_user.username + "): "+ message.text)
        await message.reply(MESSAGES_P2["part2_text_try3"])
        count_mess = 0
        await message.answer(MESSAGES_P2["part2_text_complete"], reply_markup=kb_start_p3)
    elif is_inputDonat == True:
        print(message.from_user.first_name+" ("+message.from_user.username + "): "+ message.text)
        if message.text.isdigit():
            if int(message.text) >= 10000:
                await sql_add_donat(int(message.text), message.from_user.username)
                await bot.send_message(chat_id=message.chat.id, text=MESSAGES_P3['part3_text9'].format(await sql_return_donat(message.from_user.username)), reply_markup=kb_start_p4)
                change_bool_var (False)
                await message.answer(MESSAGES_P3['part3_pay_more'])
            else:
                await message.answer(MESSAGES_P3['part3_pay_less'] + str(10000-int(message.text)) + " рублей")
        elif message.text.isdigit() == False:
            await message.answer("Это не цифры")
    else:
        print(message.from_user.first_name+" ("+message.from_user.username + "): "+ message.text)
        await message.reply("Не ломай мою программу, следуй правилам, мысли в рамках ")




def register_hendlers_part2(dp : Dispatcher):
    dp.register_message_handler(start_part2, text="Продолжить путь")
    dp.register_message_handler(next_part2, text="Начать")
    #dp.register_message_handler(chek_answer_part2)
def register_hendlers_part2_empty_handler(dp : Dispatcher):
    dp.register_message_handler(chek_text_answer)
