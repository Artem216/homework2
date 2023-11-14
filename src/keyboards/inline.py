from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# def hello_kb():
#     kb = InlineKeyboardMarkup()
#     kb.add(InlineKeyboardButton(text= "Оставить Фидбек", callback_data = "start"))
#     return kb


def ex_kb():
    kb = InlineKeyboardMarkup(one_time_keyboard=True)
    kb.add(InlineKeyboardButton(text= "Ещё одно упражнение", callback_data = "ex"))
    kb.add(InlineKeyboardButton(text= "В меню.", callback_data = "back"))