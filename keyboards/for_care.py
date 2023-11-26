from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def select_care() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Подушки")
    kb.button(text="Наматрацники")
    kb.button(text="Одеяла")
    kb.button(text="Назад")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
