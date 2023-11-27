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


@router.message(User_Status.selected_retail, F.text.lower() == "назад")
async def one_step_return(message: Message, state: FSMContext):
    await message.answer(
        "Выберите нужный пункт меню снизу👇",
        reply_markup=get_retail_or_wholesale()
    )
    await state.set_state(User_Status.start)


@router.message(User_Status.selected_opt, F.text.lower() == "назад")
async def one_step_return(message: Message, state: FSMContext):
    await message.answer(
        "Выберите нужный пункт меню снизу👇",
        reply_markup=get_retail_or_wholesale()
    )
    await state.set_state(User_Status.start)


@router.message(User_Status.selected_care_by_retail, F.text.lower() == "назад")
async def one_step_return(message: Message, state: FSMContext):
    await message.answer(
        text=" <b>«Мягкий сон» - компания с историей.</b>\n\n"
             "Сейчас это крупное предприятие, производящее тысячи единиц продукции.\n\n"
             "✅Мы производим нашу продукцию, основываясь на богатом опыте, ориентируясь на высокие современные требования рынка.\n\n"
             "<b>Мы очень рады, что Вы стали нашим покупателем 😊 и с радостью ответим на все вопросы!</b> \n\n"
             "Выберите интересующий Вас вопрос, нажатием кнопки ⬇️",
        reply_markup=select_retail_option(),
        parse_mode=ParseMode.HTML
    )
    await state.set_state(User_Status.selected_retail)


@router.message(User_Status.selected_care_by_opt, F.text.lower() == "назад")
async def one_step_return(message: Message, state: FSMContext):
    await message.answer(
        text=" <b>«Мягкий сон» - компания с историей.</b>\n\n"
             "Сейчас это крупное предприятие, производящее тысячи единиц продукции.\n\n"
             "✅Мы производим нашу продукцию, основываясь на богатом опыте, ориентируясь на высокие современные требования рынка.\n\n"
             "<b>Мы очень рады, что Вы стали нашим покупателем и надеемся на долгосрочное сотрудничество 🤝🏼</b>\n\n"
             "Выберите интересующий Вас вопрос, нажатием кнопки ⬇️",
        reply_markup=select_opt_option(),
        parse_mode=ParseMode.HTML
    )
    await state.set_state(User_Status.selected_opt)


@router.message(User_Status.end_care_by_opt, F.text.lower() == "назад")
async def care_to_opt(message: Message, state: FSMContext):
    await message.answer(
        text="Уход за какой продукцией Вас интересует ? ",
        reply_markup=select_care()
    )
    await state.set_state(User_Status.selected_care_by_opt)


@router.message(User_Status.end_care_by_retail, F.text.lower() == "назад")
async def care_to_opt(message: Message, state: FSMContext):
    await message.answer(
        text="Уход за какой продукцией Вас интересует ? ",
        reply_markup=select_care()
    )
    await state.set_state(User_Status.selected_care_by_retail)


@router.message(User_Status.end_retail, F.text.lower() == "назад")
async def one_step_return(message: Message, state: FSMContext):
    await message.answer(
        text=" <b>«Мягкий сон» - компания с историей.</b>\n\n"
             "Сейчас это крупное предприятие, производящее тысячи единиц продукции.\n\n"
             "✅Мы производим нашу продукцию, основываясь на богатом опыте, ориентируясь на высокие современные требования рынка.\n\n"
             "<b>Мы очень рады, что Вы стали нашим покупателем 😊 и с радостью ответим на все вопросы!</b> \n\n"
             "Выберите интересующий Вас вопрос, нажатием кнопки ⬇️",
        reply_markup=select_retail_option(),
        parse_mode=ParseMode.HTML
    )
    await state.set_state(User_Status.selected_retail)


@router.message(User_Status.end_opt, F.text.lower() == "назад")
async def one_step_return(message: Message, state: FSMContext):
    await message.answer(
        text=" <b>«Мягкий сон» - компания с историей.</b>\n\n"
             "Сейчас это крупное предприятие, производящее тысячи единиц продукции.\n\n"
             "✅Мы производим нашу продукцию, основываясь на богатом опыте, ориентируясь на высокие современные требования рынка.\n\n"
             "<b>Мы очень рады, что Вы стали нашим покупателем и надеемся на долгосрочное сотрудничество 🤝🏼</b>\n\n"
             "Выберите интересующий Вас вопрос, нажатием кнопки ⬇️",
        reply_markup=select_opt_option(),
        parse_mode=ParseMode.HTML
    )
    await state.set_state(User_Status.selected_opt)
