from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from handlers.status import User_Status
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from keyboards.for_opt import select_opt_option
from keyboards.for_questions import get_retail_or_wholesale
from keyboards.for_retail import select_retail_option
from keyboards.restart_menu import get_restart_menu
from keyboards.for_care import select_care

router = Router()  # [1]


@router.message(F.text.lower() == "вернуться в меню")
async def start_select(message: Message, state: FSMContext):
    await message.answer(
        "Выберите нужный пункт меню снизу👇",
        reply_markup=get_retail_or_wholesale()
    )
    await state.set_state(User_Status.start)
