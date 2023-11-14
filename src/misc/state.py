# from aiogram.fsm.context import FSMContext


from aiogram.dispatcher.filters.state import State, StatesGroup


class Ex_FSM(StatesGroup):
    ex = State()
