from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove
from handlers.status import User_Status
from keyboards.for_questions import get_retail_or_wholesale
from keyboards.for_opt import select_opt_option
from keyboards.for_retail import select_retail_option
from keyboards.start_menu import get_start_menu
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from utils.database import add_user

router = Router()  # [1]


@router.message(Command("start"))  # [2]
async def cmd_start(message: Message, state: FSMContext):
    user = message.from_user
    msg = await message.answer("Запускаем нашего бота для Вас...")
    add_user(user)
    await msg.delete()
    await message.answer(
        "Привет! На связи команда «Мягкий сон»! Мы сделали этого бота, что бы Вы смогли решать все Ваши вопросы 24/7. Это очень удобно👏\n\n"
        "С помощью данного бота Вы можете связаться с поддержкой!",
        reply_markup=get_start_menu()
    )
    await message.delete()
    await state.clear()


@router.message(StateFilter(None), F.text.lower() == "начать")
async def start_select(message: Message, state: FSMContext):
    await message.answer(
        "Выберите нужный пункт меню снизу👇",
        reply_markup=get_retail_or_wholesale()
    )
    await state.set_state(User_Status.start)



@router.message(User_Status.start, F.text.lower() == "опт")
async def answer_opt(message: Message, state: FSMContext):
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


@router.message(User_Status.start, F.text.lower() == "розница")
async def answer_retail(message: Message, state: FSMContext):
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