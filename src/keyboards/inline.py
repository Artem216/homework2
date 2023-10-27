from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



def hello_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text= "Оставить Фидбек", callback_data = "start"))
    return kb