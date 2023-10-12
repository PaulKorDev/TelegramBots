from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#Buttons
circle_inkb_but1 = InlineKeyboardButton(text="Возбуждение", callback_data="circle_callback1")
circle_inkb_but2 = InlineKeyboardButton(text="Мать", callback_data="circle_callback2")
circle_inkb_but3 = InlineKeyboardButton(text="\"Колеса\"", callback_data="circle_callback3")

family_inkb_but1 = InlineKeyboardButton(text="Сжечь", callback_data="family_callback1")
family_inkb_but2 = InlineKeyboardButton(text="Реклама", callback_data="family_callback2")
family_inkb_but3 = InlineKeyboardButton(text="Страх", callback_data="family_callback3")

list_inkb_but1 = InlineKeyboardButton(text="Марихуана", callback_data="list_callback1")
list_inkb_but2 = InlineKeyboardButton(text="Половые губы", callback_data="list_callback2")
list_inkb_but3 = InlineKeyboardButton(text="Лесополоса", callback_data="list_callback3")

dog_inkb_but1 = InlineKeyboardButton(text="Моча", callback_data="dog_callback1")
dog_inkb_but2 = InlineKeyboardButton(text="Любовница", callback_data="dog_callback2")
dog_inkb_but3 = InlineKeyboardButton(text="Река/бочка", callback_data="dog_callback3")

baby_inkb_but1 = InlineKeyboardButton(text="Похищение", callback_data="baby_callback1")
baby_inkb_but2 = InlineKeyboardButton(text="Эрекция", callback_data="baby_callback2")
baby_inkb_but3 = InlineKeyboardButton(text="Поход за хлебом", callback_data="baby_callback3")

train_inkb_but1 = InlineKeyboardButton(text="Безнадежность", callback_data="train_callback1")
train_inkb_but2 = InlineKeyboardButton(text="Шлюха", callback_data="train_callback2")
train_inkb_but3 = InlineKeyboardButton(text="Анал без смазки", callback_data="train_callback3")

#buts for slider
slider_but_next = InlineKeyboardButton(text=">>", callback_data="slider_next_callback")
slider_but_prev = InlineKeyboardButton(text="<<", callback_data="slider_prev_callback")

#buts for true false
true_but = InlineKeyboardButton(text="Правда", callback_data="true_callback")
false_but = InlineKeyboardButton(text="Ложь", callback_data="false_callback")

#buts for mark
one_but = InlineKeyboardButton(text="1️⃣", callback_data="mark_1_callback")
two_but = InlineKeyboardButton(text="2️⃣", callback_data="mark_2_callback")
three_but = InlineKeyboardButton(text="3️⃣", callback_data="mark_3_callback")
four_but = InlineKeyboardButton(text="4️⃣", callback_data="mark_4_callback")
five_but = InlineKeyboardButton(text="5️⃣", callback_data="mark_5_callback")

#buts fo pay messages
want_but = InlineKeyboardButton(text="Да", callback_data="want_callback")
nowant_but = InlineKeyboardButton(text="Нет", callback_data="nowant_callback")

#buts for scam kurs
yes_but = InlineKeyboardButton(text="Я скинул", callback_data="skinul_callback")


#murkups
circle_inkb = InlineKeyboardMarkup(row_width=3)
family_inkb = InlineKeyboardMarkup(row_width=3)
list_inkb = InlineKeyboardMarkup(row_width=3)
dog_inkb = InlineKeyboardMarkup(row_width=3)
baby_inkb = InlineKeyboardMarkup(row_width=3)
train_inkb = InlineKeyboardMarkup(row_width=3)

slider_inkb = InlineKeyboardMarkup(row_width=2)

trueFalse_inkb = InlineKeyboardMarkup(row_width=2)

marks_inkb = InlineKeyboardMarkup(row_width=5)

donat_inkb = InlineKeyboardMarkup(row_width=2)

kurs_inkb = InlineKeyboardMarkup(row_width=1)

#add buttons to keyboards
kurs_inkb.add(yes_but)

donat_inkb.row(
    want_but,
    nowant_but
)

slider_inkb.row(
    slider_but_prev,
    slider_but_next
    )

trueFalse_inkb.row(
    true_but,
    false_but
)

marks_inkb.row(
    one_but,
    two_but,
    three_but,
    four_but,
    five_but
)

circle_inkb.row(
    circle_inkb_but1,
    circle_inkb_but2,
    circle_inkb_but3
    )

family_inkb.row(
    family_inkb_but1,
    family_inkb_but2,
    family_inkb_but3
    )

list_inkb.row(
    list_inkb_but1,
    list_inkb_but2,
    list_inkb_but3
    )

dog_inkb.row(
    dog_inkb_but1,
    dog_inkb_but2,
    dog_inkb_but3
    )

baby_inkb.row(
    baby_inkb_but1,
    baby_inkb_but2,
    baby_inkb_but3
    )

train_inkb.row(
    train_inkb_but1,
    train_inkb_but2,
    train_inkb_but3
    )