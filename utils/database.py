from typing import Dict, List, Union
import pygsheets
from bot import wks
from aiogram.types import Message


def add_user(user):
    username = "https://t.me/" + user.username
    id = user.id
    firstname = user.first_name
    lastname = user.last_name
    if not check_user(id):
        return
    column_a = wks.get_col(1, include_tailing_empty=False)
    filled_fields = len(column_a)
    wks.update_value(f'A{str(filled_fields + 1)}', f"{username}")
    wks.update_value(f'B{str(filled_fields + 1)}', f"{id}")
    wks.update_value(f'C{str(filled_fields + 1)}', f"{firstname}")
    wks.update_value(f'D{str(filled_fields + 1)}', f"{lastname}")

def check_user(user_id):
    column_b = wks.get_col(2, include_tailing_empty=False)
    if str(user_id) not in column_b:
        return True
    else:
        return False

