from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from handlers.status import User_Status
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from keyboards.restart_menu import get_restart_menu

router = Router()  # [1]


@router.message(User_Status.choosing_retail, F.text.lower() == "уход")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="БЛЯ КАКОЙ ЖЕ ЕБЕЙШИЙ ТЕКСТ ПРО УХОД ДЛЯ РОЗНИЦЫ Я НЕ МОГУ",
        reply_markup=get_restart_menu()
    )
    await state.clear()


@router.message(User_Status.choosing_retail, F.text.lower() == "брак по товару")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="БРАТАНЧИК, ОБРАТИСЬ В ПОДДЕРЖКУ НО ПОНИМАЙ ЧТО НАМ НУЖНЫ ФОТКИ ИЛИ ВИДОС КОТОРЫЙ ПОДТВЕРЖАЕТ ЧТО ТЫ НЕ "
             "ПИДОРАС. ВОТ ССЫЛКА НА ПОДДЕРЖКУ @horoz25",
        reply_markup=get_restart_menu()
    )
    await state.clear()


@router.message(User_Status.choosing_retail, F.text.lower() == "ассортимент")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="БЛЯ КАКОЙ ЖЕ ЕБЕЙШИЙ ТЕКСТ ПРО АССОРТИМЕНТ ДЛЯ РОЗНИЦЫ Я НЕ МОГУ",
        reply_markup=get_restart_menu()
    )
    await state.clear()


@router.message(User_Status.choosing_retail, F.text.lower() == "акции/скидки")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="БЛЯ КАКОЙ ЖЕ ЕБЕЙШИЙ ТЕКСТ ПРО СКИДКИ ДЛЯ РОЗНИЦЫ Я НЕ МОГУ",
        reply_markup=get_restart_menu()
    )
    await state.clear()
