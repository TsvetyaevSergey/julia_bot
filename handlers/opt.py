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
        text="Не готовый текст про УХОД ОПТ",
        reply_markup=get_restart_menu()
    )
    await state.clear()


@router.message(User_Status.choosing_opt, F.text.lower() == "брак по товару")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="Очень жаль, что что-то пошло не так 😞\n"
        "Не спешите оставлять плохой отзыв, мы очень дорожим нашими клиентами и нашим рейтингом! \n"
        "Опишите Вашу ситуацию консультанту по ссылке ниже 👇 мы обязательно поможем решить Ваш вопрос! \n"
        "✅ не забудьте приложить фотографии/видео\n"
        "@softsleep_online",
        reply_markup=get_restart_menu()
    )
    await state.clear()


@router.message(User_Status.choosing_opt, F.text.lower() == "переход на сайт")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="Для того, чтобы подробнее ознакомиться с нашим ассортиментом переходите по ссылке 😇 \n"
        "Желаем отличных покупок! \n"
        "https://www.softdream.ru/?ysclid=lpb5q2rc5e789037866\n",
        reply_markup=get_restart_menu()
    )
    await state.clear()

