from aiogram.fsm.state import StatesGroup, State


class User_Status(StatesGroup):
    start = State()
    selected_opt = State()
    selected_retail = State()
    selected_care_by_opt = State()
    selected_care_by_retail = State()
    end_care_by_opt = State()
    end_care_by_retail = State()
    end_opt = State()
    end_retail = State()
