from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_restart_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)