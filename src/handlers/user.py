from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext


from ..db.crud import get_db, save_answer, get_user,create_user, get_user_answer


from ..keyboards.reply import main_kb, ex_kb
from ..keyboards.inline import goal_kb, change_kb


from ..misc.state import Ex_FSM, Form
from ..misc.texts import text_ex, text_menu, text_motivation




async def start(msg: Message, state : FSMContext):
    db = next(get_db())
    # print(get_user(db, msg))
    user1 = get_user(db, msg.from_user.id)
    if user1 is None:
        user = create_user(db, msg)
        await msg.answer(text=f"Привет, {msg.from_user.first_name}! Давай заполним начальные данные для отслеживания прогресса и подбора программы тренировок и питания!\n\n Напиши свой рост в сантиметрах!")
        await state.set_state(Form.height) 
    else:
        await msg.answer(text= f"Привет, {msg.from_user.first_name}! Твой аккаунт уже привязан к боту.", reply_markup=main_kb())


async def get_height(msg: Message, state: FSMContext):
    text = msg.text
    if text.isdigit() and int(text) < 230 and int(text) > 100:
        db = next(get_db())
        ans = get_user_answer(db, msg.from_user.id)
        ans.height = int(text)
        save_answer(db, ans)
        await msg.answer(text=f"Теперь пришли свой вес в кг.")
        await state.set_state(Form.weight)
    else: 
        await msg.answer(text=f"Введён неправильный формат данных! Введите заново.")
    

async def get_weight(msg: Message, state: FSMContext):
    text = msg.text
    if text.isdigit() and int(text) < 350 and int(text) > 30:
        db = next(get_db())
        ans = get_user_answer(db, msg.from_user.id)
        ans.weight = int(text)
        save_answer(db, ans)
        await msg.answer(text=f"Какая твоя цель тренировок.", reply_markup=goal_kb())
        await state.set_state(Form.goal)
    else: 
        await msg.answer(text=f"Введён неправильный формат данных! Введите заново.")
    

async def get_goal(call: CallbackQuery, state: FSMContext):
    data = call.data
    db = next(get_db())
    ans = get_user_answer(db, call.from_user.id)
    if data == "mass":
        ans.goal = True
    else: 
        ans.goal = False
    save_answer(db, ans)
    await call.message.answer(text= "Данные обновлены!",reply_markup=main_kb())
    await state.finish()



async def dayly_ex(msg: Message, state : FSMContext):
    await msg.answer(text=text_ex(True), reply_markup=ex_kb())
    await state.set_state(Ex_FSM.ex)


async def more_dayly_ex(msg: Message, state : FSMContext):
    if msg.text == "Ещё одно упражнение":
        await msg.answer(text=text_ex(False), reply_markup=ex_kb())
    if msg.text == "В меню":
        await msg.answer(text="Возврат в меню.", reply_markup=main_kb())
        await state.finish()


async def character_menu(msg: Message, state : FSMContext):
    db = next(get_db())
    ans = get_user_answer(db, msg.from_user.id)
    print(ans.goal)
    goal = 'Набрать массу' if ans.goal else 'Похудеть'
    await msg.answer(text=f"Ваш профиль:\n\n Вес: {ans.weight}\n\n Рост: {ans.height}\n\n Цель: {goal}", reply_markup=change_kb())


async def change_height(call: CallbackQuery, state: FSMContext):
    if call.data == "change":
        await state.set_state(Form.height)
        await call.message.answer(text='Введи свой рост:')
    else: 
        await call.message.answer("Возврат в меню.",reply_markup=main_kb())

async def dayly_menu(msg: Message, state : FSMContext):
    await msg.answer(text=text_menu(msg.from_user.id), reply_markup=main_kb())
    

async def motivation(msg: Message, state : FSMContext):
    await msg.answer(text=text_motivation(), reply_markup=main_kb())





def register_user(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"], state= "*")

    dp.register_message_handler(get_height,state=Form.height)
    dp.register_message_handler(get_weight,state=Form.weight)
    dp.register_callback_query_handler(get_goal,state=Form.goal)
    dp.register_callback_query_handler(change_height, lambda call: call.data == "change" or "menu", state= '*')

    dp.register_message_handler(more_dayly_ex,lambda msg: msg.text == "В меню" or "Ещё одно упражнение", state=Ex_FSM.ex)
    dp.register_message_handler(character_menu,lambda msg: msg.text == "Мой профиль.", state= '*')
    dp.register_message_handler(dayly_ex,lambda msg: msg.text == "Упражнение дня." , state= "*")
    dp.register_message_handler(dayly_menu,lambda msg: msg.text == "Меню на день" , state= "*")
    dp.register_message_handler(motivation,lambda msg: msg.text == "Мотивационное сообщение!" , state= "*")
