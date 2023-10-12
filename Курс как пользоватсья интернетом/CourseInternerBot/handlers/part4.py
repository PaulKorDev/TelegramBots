from messages import MESSAGES_P4
from config import count_testq, real_mark
from database.sqlite_db import sql_add_part, sql_add_mark, sql_return_donat
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from keyboards.in_kb import trueFalse_inkb, marks_inkb, donat_inkb, kurs_inkb
from keyboards.kb import kb_to_pay
from create_bot import bot
from os import remove, path

import cv2

async def start_part4 (message: types.Message):
    await sql_add_part(4, message.from_user.username)
    print(message.from_user.first_name+" ("+message.from_user.username + "): "+ "part4-test")

    await message.answer(MESSAGES_P4['part4_text'].format(message.from_user.first_name), reply_markup=ReplyKeyboardRemove())
    await message.answer('Тест:')
    await message.answer(MESSAGES_P4['part4_test_q1'], reply_markup=trueFalse_inkb)

async def start_end (message: types.Message):
    print(message.from_user.first_name+" ("+message.from_user.username + "): "+ "на оплате чека")
    await message.answer('Небольшой факт: ученые выяснили, что люди, которые вознаграждают людей за их труды, живут счастливее', reply_markup=ReplyKeyboardRemove())
    await message.answer('Вы хотите оплатить чек на {0} руб?'.format(str(int(await sql_return_donat(message.from_user.username))*2)), reply_markup=donat_inkb)


async def true_chek(callback : types.CallbackQuery):
    global count_testq
    await callback.answer(MESSAGES_P4['part4_test_t' + str(count_testq)], show_alert=True)
    count_testq += 1
    print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+ "testq-"+str(count_testq))
    if count_testq == 6:
        count_testq = 1
        await bot.edit_message_text(MESSAGES_P4['end_text'], callback.message.chat.id, callback.message.message_id)
        #сертефикат
        img = cv2.imread('img\sertificat.png')
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, callback.from_user.first_name.upper(), (377, 118), font, 2, (0,0,0), 2)
        cv2.imwrite('certificate_done.jpg', img)

        img = open('certificate_done.jpg', 'rb')
        await bot.send_photo(callback.message.chat.id, img)

        await callback.message.answer("Теперь ставьте оценку", reply_markup=marks_inkb)

        if path.isfile('certificate_done.jpg'): 
            remove('certificate_done.jpg') 
            print("success") 
        else: 
            print("File doesn't exists!")
        

    else:
        await bot.edit_message_text(MESSAGES_P4['part4_test_q' + str(count_testq)], callback.message.chat.id, callback.message.message_id, reply_markup=trueFalse_inkb)

async def false_chek(callback : types.CallbackQuery):
    global count_testq
    await callback.answer(MESSAGES_P4['part4_test_f' + str(count_testq)], show_alert=True)
    print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+ "testF-"+MESSAGES_P4['part4_test_f' + str(count_testq)])
    

async def mark_chek(callback : types.CallbackQuery):
    global real_mark
    if (callback.data == 'mark_1_callback'):
        if real_mark == 1:
            await sql_add_mark(1, callback.from_user.username)
            real_mark = 0
        await callback.answer(text='Вы наверное имели ввиду 1, как первый - самый лучший', show_alert=True)
    elif (callback.data == 'mark_2_callback'):
        if real_mark == 2:
            await sql_add_mark(1, callback.from_user.username)
            real_mark = 0
        await callback.answer(text='Боюсь этого мало', show_alert=True)
    elif (callback.data == 'mark_3_callback'):
        if real_mark == 3:
            await sql_add_mark(1, callback.from_user.username)
            real_mark = 0
        await callback.answer(text='Вы слишком занизили, попробуйте еще раз', show_alert=True)
    elif (callback.data == 'mark_4_callback'):
        if real_mark == 4:
            await sql_add_mark(1, callback.from_user.username)
            real_mark = 0
        await callback.answer(text='Вы промазали, попробуйте еще раз', show_alert=True)
    elif (callback.data == 'mark_5_callback'):
        if real_mark == 5:
            await sql_add_mark(1, callback.from_user.username)
            real_mark = 0
        await callback.message.answer(text='Я рад, что вам понравился наш тренинг, еще никто его не оценивал ниже 5, это потому что он менят жизни людей.', reply_markup=kb_to_pay)
        await callback.answer()
    print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+ "mark-"+callback.data)

async def yes_donat(callback : types.CallbackQuery):
    print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+ "chek-"+"решил оплатить")
    await callback.message.answer('Будем честны, у вас нет таких денег, но я уважаю ваше желание поступить правильно, поэтому кидайте сюда, всё, что у вас есть: 5469 5500 5257 8686')

async def no_donat(callback : types.CallbackQuery):
    print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+ "chek-"+"решил не платить")
    await callback.message.answer('Я не уважаю ваш выбор')
    await callback.message.answer('Не хотите пройти наш новый курс \"Виды мошенничества, почему не стоит скидывать деньги на карту незнакомым людям и как не стать жертвой \", стоимость курса - бесплатно*?\n\n*для инвалидов и ветеранов войны, для остальных 100 рублей. \nКидать на карту: 5469 5500 5257 8686', reply_markup=kurs_inkb)

async def skinul_donat(callback : types.CallbackQuery):
    await callback.message.answer('Пока')
    print(callback.message.from_user.first_name+" ("+callback.message.from_user.username + "): "+ "scam-"+"попался")


def register_hendlers_part4(dp : Dispatcher):
    dp.register_message_handler(start_part4, text= "Возрадоваться и продолжить")
    dp.register_message_handler(start_end, text="С удовольствием перейти к оплате чека")

    #callbacks
    dp.register_callback_query_handler(callback=true_chek, text="true_callback")
    dp.register_callback_query_handler(callback=false_chek, text="false_callback")
    dp.register_callback_query_handler(callback=yes_donat, text="want_callback")
    dp.register_callback_query_handler(callback=no_donat, text="nowant_callback")
    dp.register_callback_query_handler(callback=skinul_donat, text="skinul_callback")
    dp.register_callback_query_handler(mark_chek, lambda x: x.data and x.data.startswith('mark_') )