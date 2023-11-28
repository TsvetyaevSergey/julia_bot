from aiogram.types import ReplyKeyboardMarkup
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_help():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Написать в поддержку",
        url=f"tg://user?id=6954613050")
    )
    return builder.as_markup()
