from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



def main_kb():
    kb = ReplyKeyboardMarkup(True, True, one_time_keyboard=True)
    kb.row("Упражнение дня.", "Меню на день")
    kb.add(KeyboardButton("Мотивационное сообщение!"))
    kb.add(KeyboardButton("Мой профиль."))
    return kb


def ex_kb():
    kb = ReplyKeyboardMarkup(True, True, one_time_keyboard=True)
    kb.add(KeyboardButton(text= "Ещё одно упражнение"))
    kb.add(KeyboardButton(text= "В меню"))
    return kb