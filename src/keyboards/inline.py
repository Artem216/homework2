from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# def hello_kb():
#     kb = InlineKeyboardMarkup()
#     kb.add(InlineKeyboardButton(text= "Оставить Фидбек", callback_data = "start"))
#     return kb


# def ex_kb():
#     kb = InlineKeyboardMarkup(one_time_keyboard=True)
#     kb.add(InlineKeyboardButton(text= "Ещё одно упражнение", callback_data = "ex"))
#     kb.add(InlineKeyboardButton(text= "В меню.", callback_data = "back"))


def goal_kb():
    kb = InlineKeyboardMarkup(one_time_keyboard=True)
    kb.add(InlineKeyboardButton(text= "Набрать массу.", callback_data = "mass"))
    kb.add(InlineKeyboardButton(text= "Похудеть", callback_data = "fit"))
    return kb

def change_kb():
    kb = InlineKeyboardMarkup(one_time_keyboard=True)
    kb.add(InlineKeyboardButton(text= "Изменить данные", callback_data = "change"))
    kb.add(InlineKeyboardButton(text= "Обратно в меню", callback_data = "menu"))
    return kb