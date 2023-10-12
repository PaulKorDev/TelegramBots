from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""
#Buttons
but = InlineKeyboardButton(text="pattern", callback_data="pattern_callback")

#keyboard init
in_kb_pattern = InlineKeyboardMarkup(row_width=1)

#add buttons to keyboards
in_kb_pattern.add(but)


def create_in_kb_pattern (a, b):    
    in_kb_create = InlineKeyboardMarkup(row_width=1)
    in_kb_create.add(InlineKeyboardButton(text=f"{a}", callback_data=f"{b}_callback"))
    return in_kb_create
"""
    
#Full string
#InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text="", callback_data="_callback"))
