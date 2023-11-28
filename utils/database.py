from typing import Dict, List, Union
import pygsheets
from bot import wks
from aiogram.types import Message


def add_user(user):
    if str(user.username) == "None":
        username = "Приватный аккаунт"
    else:
        username = "https://t.me/" + str(user.username)
    id = user.id
    firstname = user.first_name
    if str(user.last_name) == "None":
        lastname = "Фамилия не указана"
    else:
        lastname = user.last_name
    if not check_user(id):
        return
    column_a = wks.get_col(1, include_tailing_empty=False)
    filled_fields = len(column_a)
    wks.update_value(f'A{str(filled_fields + 1)}', f"{str(username)}")
    wks.update_value(f'B{str(filled_fields + 1)}', f"{str(id)}")
    wks.update_value(f'C{str(filled_fields + 1)}', f"{str(firstname)}")
    wks.update_value(f'D{str(filled_fields + 1)}', f"{str(lastname)}")

def check_user(user_id):
    column_b = wks.get_col(2, include_tailing_empty=False)
    if str(user_id) not in column_b:
        return True
    else:
        return False

