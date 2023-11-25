from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def select_opt_option() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Уход")
    kb.button(text="Брак по товару")
    kb.button(text="Переход на сайт")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
