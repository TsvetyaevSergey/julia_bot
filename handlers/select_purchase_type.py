from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from handlers.status import User_Status
from keyboards.for_questions import get_retail_or_wholesale
from keyboards.for_opt import select_opt_option
from keyboards.for_retail import select_retail_option
from keyboards.start_menu import get_start_menu
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

router = Router()  # [1]


@router.message(Command("start"))  # [2]
async def cmd_start(message: Message,state: FSMContext):
    await message.answer(
        "Привет!\nНа связи команда «Мягкий сон»! Мы сделали этого бота, что бы Вы смогли решать все Ваши вопросы 24/7.\n"
        "Это очень удобно👏\n"
        "С помощью данного бота Вы можете связаться с поддержкой!\n"
        "Готовы начать?",
        reply_markup=get_start_menu()
    )


@router.message(StateFilter(None), F.text.in_(["Начать", "Вернуться в меню"]))
async def start_select(message: Message, state: FSMContext):
    await message.answer(

        "Выберите нужный пункт меню снизу👇",
        reply_markup=get_retail_or_wholesale()
    )
    await state.set_state(User_Status.start)


@router.message(User_Status.start, F.text.lower() == "опт")
async def answer_opt(message: Message, state: FSMContext):
    await message.answer(
        "ТУТ БУДЕТ ЕБЕЙШИЙ ТЕКСТ ПРО ОПТ",
        reply_markup=select_opt_option()
    )
    await state.set_state(User_Status.choosing_opt)


@router.message(User_Status.start, F.text.lower() == "розница")
async def answer_retail(message: Message, state: FSMContext):
    await message.answer(
        "ТУТ БУДЕТ ЕБЕЙШИЙ ТЕКСТ ПРО РОЗНИЦУs",
        reply_markup=select_retail_option()
    )
    await state.set_state(User_Status.choosing_retail)
