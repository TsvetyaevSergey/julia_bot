from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_retail_or_wholesale() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="ОПТ")
    kb.button(text="Розница")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)