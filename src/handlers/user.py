import httpx
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
# from aiogram.fsm.context import FSMContext

import json
import random
import datetime


from ..keyboards.reply import main_kb, ex_kb
# from ..keyboards.inline import ex_kb


from ..misc.state import Ex_FSM


def text_ex(flag: bool) -> str:
    if flag:
        if datetime.datetime.now().day == 31:
            number = int(datetime.datetime.now().day / 2) - 1
        else:
            number = int(datetime.datetime.now().day / 2)
            with open('base.json') as f:
                templates = json.load(f)
                ans = f"Упражниние дня!\n\n{templates[number - 1]['name']}\n\nРабочая группа мышц: {templates[number - 1]['muscules']}\n\nТехника выполнения: {templates[number - 1]['descr']}"
                return ans
    else:
        number = random.randint(2, 16)
        with open('base.json') as f:
                templates = json.load(f)
                ans = f"Упражниние дня!\n\n{templates[number - 1]['name']}\n\nРабочая группа мышц: {templates[number - 1]['muscules']}\n\nТехника выполнения: {templates[number - 1]['descr']}"
                return ans

def text_menu() -> str:
    day = datetime.datetime.now()
    number = day.weekday()
    with open('menu.json') as f:
        templates = json.load(f)
        ans = f"Завтрак: {templates[number]['brkf']}\n\nОбед: {templates[number]['lunch']}\n\nПолдник: {templates[number]['poldnik']}\n\nУжин: {templates[number]['dinner']}"
        return ans


def text_motivation() -> str:
    number = random.randint(0, 13)
    with open('motivation.json') as f:
            templates = json.load(f)
            ans = templates[number]['text']
            return ans



async def start(msg: Message, state : FSMContext):
    await msg.answer(text= f"Привет, {msg.from_user.first_name}! Твой аккаунт успешно привязан к боту.", reply_markup=main_kb())
    

async def dayly_ex(msg: Message, state : FSMContext):
    await msg.answer(text=text_ex(True), reply_markup=ex_kb())
    await state.set_state(Ex_FSM.ex)


async def more_dayly_ex(msg: Message, state : FSMContext):
    if msg.text == "Ещё одно упражнение":
        await msg.answer(text=text_ex(False), reply_markup=ex_kb())
    if msg.text == "В меню":
        await msg.answer(text="Возврат в меню.", reply_markup=main_kb())
        await state.finish()



async def dayly_menu(msg: Message, state : FSMContext):
    await msg.answer(text=text_menu(), reply_markup=main_kb())
    

async def motivation(msg: Message, state : FSMContext):
    await msg.answer(text=text_motivation(), reply_markup=main_kb())





def register_user(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"], state= "*")
    dp.register_message_handler(dayly_ex,lambda msg: msg.text == "Упражнение дня." , state= "*")
    dp.register_message_handler(more_dayly_ex,lambda msg: msg.text == "В меню" or "Ещё одно упражнение", state=Ex_FSM.ex)
    dp.register_message_handler(dayly_menu,lambda msg: msg.text == "Меню на день" , state= "*")
    dp.register_message_handler(motivation,lambda msg: msg.text == "Мотивационное сообщение!" , state= "*")
