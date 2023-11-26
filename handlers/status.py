from aiogram.fsm.state import StatesGroup, State


class User_Status(StatesGroup):
    start = State()
    choosing_opt = State()
    choosing_retail = State()
    choosing_care = State()
