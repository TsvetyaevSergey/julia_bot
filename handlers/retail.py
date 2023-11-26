from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from keyboards.restart_menu import get_restart_menu
from keyboards.for_care import select_care
from handlers.status import User_Status

router = Router()  # [1]


@router.message(User_Status.choosing_retail, F.text.lower() == "уход")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="Уход за какой продукцией Вас интересует ? ",
        reply_markup=select_care()
    )
    await state.set_state(User_Status.choosing_care)


@router.message(User_Status.choosing_retail, F.text.lower() == "брак по товару")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="Очень жаль, что что-то пошло не так 😞\n\n"
        "Не спешите оставлять плохой отзыв, мы очень дорожим нашими клиентами и нашим рейтингом! \n\n"
        "Опишите Вашу ситуацию консультанту по ссылке ниже 👇 мы обязательно поможем решить Ваш вопрос! \n\n"
        "✅ не забудьте приложить фотографии/видео\n\n"
        "@softsleep_online",
        reply_markup=get_restart_menu()
    )
    await state.clear()


@router.message(User_Status.choosing_retail, F.text.lower() == "ассортимент")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="Весь наш ассортимент вы можете увидеть, перейдя по ссылкам ниже ⬇️ \n\n"
        "OZON 🤩✅\n"
        "https://ozon.ru/t/KyjM0go\n\n"
        "WILDBERRIES 🤩 🚀 \n"
        "https://www.wildberries.ru/seller/18659\n\n"
        "ЯНДЕКС. МАРКЕТ 🤩🔥\n"
        "https://market.yandex.ru/business--ooo-miagkii-son/4831922\n\n"
        "Порадуйте себя и своих близких отличным подарком 🎁",
        reply_markup=get_restart_menu()
    )
    await state.clear()


@router.message(User_Status.choosing_retail, F.text.lower() == "акции/скидки")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="Помимо большого ассортиментного выбора и выгодных цен, мы готовимся к Новогоднему сезону ⛄️❄️\n"
        "А это значит, что цены будут ЕЩЕ ВЫГОДНЕЕ. \n"
        "Порадуйте себя и своих близких отличным подарком 🎁\n"
        "Нашу продукцию Вы можете найти по ссылкам:\n\n"
        "OZON 🤩✅\n"
        "https://ozon.ru/t/KyjM0go\n\n"
        "WILDBERRIES 🤩 🚀 \n"
        "https://www.wildberries.ru/seller/18659\n\n"
        "ЯНДЕКС. МАРКЕТ 🤩🔥\n"
        "https://market.yandex.ru/business--ooo-miagkii-son/4831922",
        reply_markup=get_restart_menu()
    )
    await state.clear()

@router.message(User_Status.choosing_retail, F.text.lower() == "переход на сайт")
async def select_uhod(message: Message, state: FSMContext):
    await message.answer(
        text="Для того, чтобы подробнее ознакомиться с нашим ассортиментом, переходите по ссылке и подписывайтесь на наши магазины ! 😇 \n"
        "Мы сохраняем выгодные цены для наших покупателей.\n"
        "Желаем отличных покупок!\n\n"
        "OZON 🤩✅\n"
        "https://ozon.ru/t/KyjM0go\n\n"
        "WILDBERRIES 🤩 🚀 \n"
        "https://www.wildberries.ru/seller/18659\n\n"
        "ЯНДЕКС. МАРКЕТ 🤩🔥\n"
        "https://market.yandex.ru/business--ooo-miagkii-son/4831922",
        reply_markup=get_restart_menu()
    )
    await state.clear()

