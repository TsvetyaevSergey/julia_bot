from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from handlers.status import User_Status
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from keyboards.restart_menu import get_restart_menu

router = Router()  # [1]


@router.message(User_Status.choosing_opt, F.text.lower() == "уход")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="БЛЯ КАКОЙ ЖЕ ЕБЕЙШИЙ ТЕКСТ ПРО УХОД ДЛЯ ОПТА Я НЕ МОГУ",
        reply_markup=get_restart_menu()
    )
    await state.clear()


@router.message(User_Status.choosing_opt, F.text.lower() == "брак по товару")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="БЛЯ КАКОЙ ЖЕ ЕБЕЙШИЙ ТЕКСТ ПРО БРАК ДЛЯ ОПТА Я НЕ МОГУ",
        reply_markup=get_restart_menu()
    )
    await state.clear()


@router.message(User_Status.choosing_opt, F.text.lower() == "переход на сайт")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="БЛЯ КАКОЙ ЖЕ ЕБЕЙШИЙ ТЕКСТ ПРО САЙТ ДЛЯ ОПТА Я НЕ МОГУ",
        reply_markup=get_restart_menu()
    )
    await state.clear()

