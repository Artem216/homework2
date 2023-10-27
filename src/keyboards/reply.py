from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



def main_kb():
    kb = ReplyKeyboardMarkup(True, True)
    kb.row("Упражнение дня.", "Меню на день")
    kb.add(KeyboardButton("Мотивационное сообщение!"))
    return kb