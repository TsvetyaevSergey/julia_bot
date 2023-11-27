from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from keyboards.restart_menu import get_restart_menu
from keyboards.for_care import select_care
from keyboards.for_questions import get_retail_or_wholesale
from handlers.status import User_Status

router = Router()  # [1]


@router.message(User_Status.selected_retail, F.text.lower() == "уход")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="Уход за какой продукцией Вас интересует ? ",
        reply_markup=select_care()
    )
    await state.set_state(User_Status.selected_care_by_retail)


@router.message(User_Status.selected_retail, F.text.lower() == "брак по товару")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="<b>Очень жаль, что что-то пошло не так 😞</b>\n\n"
             "Не спешите оставлять плохой отзыв, мы очень дорожим нашими клиентами и нашим рейтингом! \n\n"
             "Опишите Вашу ситуацию консультанту по ссылке ниже 👇 мы обязательно поможем решить Ваш вопрос! \n\n"
             "<b>✅ не забудьте приложить фотографии/видео</b>\n\n"
             "Написать в поддержку @softsleep_online",
        reply_markup=get_restart_menu(),
        parse_mode = ParseMode.HTML
    )
    await state.set_state(User_Status.end_retail)


@router.message(User_Status.selected_retail, F.text.lower() == "ассортимент")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="<b>Весь наш ассортимент вы можете увидеть, перейдя по ссылкам ниже ⬇️ </b>\n\n"
             "OZON 🤩✅\n"
             "https://ozon.ru/t/KyjM0go\n\n"
             "WILDBERRIES 🤩 🚀 \n"
             "https://www.wildberries.ru/seller/18659\n\n"
             "ЯНДЕКС. МАРКЕТ 🤩🔥\n"
             "https://market.yandex.ru/business--ooo-miagkii-son/4831922\n\n"
             "Порадуйте себя и своих близких отличным подарком 🎁",
        reply_markup=get_restart_menu(),
        parse_mode=ParseMode.HTML
    )
    await state.set_state(User_Status.end_retail)


@router.message(User_Status.selected_retail, F.text.lower() == "акции/скидки")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="Помимо большого ассортиментного выбора и выгодных цен, мы готовимся к Новогоднему сезону ⛄️❄️\n"
             "А это значит, что цены будут ЕЩЕ ВЫГОДНЕЕ. \n\n"
             "<b>Порадуйте себя и своих близких отличным подарком 🎁</b>\n\n"
             "<b>Нашу продукцию Вы можете найти по ссылкам:</b>\n\n"
             "OZON 🤩✅\n"
             "https://ozon.ru/t/KyjM0go\n\n"
             "WILDBERRIES 🤩 🚀 \n"
             "https://www.wildberries.ru/seller/18659\n\n"
             "ЯНДЕКС. МАРКЕТ 🤩🔥\n"
             "https://market.yandex.ru/business--ooo-miagkii-son/4831922",
        reply_markup=get_restart_menu(),
        parse_mode=ParseMode.HTML

    )
    await state.set_state(User_Status.end_retail)




