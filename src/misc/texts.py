import json
import random
import datetime

from ..db.crud import get_db, save_answer, get_user,create_user, get_user_answer


def text_ex(flag: bool) -> str:
    if flag:
        if datetime.datetime.now().day == 31:
            number = int(datetime.datetime.now().day / 2) - 1
        else:
            number = int(datetime.datetime.now().day / 2)
            with open('base.json') as f:
                templates = json.load(f)
                ans = f"Упражниние дня!\n\n{templates[number - 1]['name']}\n\nРабочая группа мышц: {templates[number - 1]['muscules']}\n\nТехника выполнения: {templates[number - 1]['descr']}"
                return ans
    else:
        number = random.randint(2, 16)
        with open('base.json') as f:
                templates = json.load(f)
                ans = f"Упражниние дня!\n\n{templates[number - 1]['name']}\n\nРабочая группа мышц: {templates[number - 1]['muscules']}\n\nТехника выполнения: {templates[number - 1]['descr']}"
                return ans

def text_menu(msg_id) -> str:
    db = next(get_db())
    ans = get_user_answer(db, msg_id)
    if ans.goal == 0:
         file = 'menu_fit.json'
    else:
         file = 'menu_mass.json'
    day = datetime.datetime.now()
    goal = 'набора массы' if ans.goal else 'похудения' 
    number = day.weekday()
    with open(file) as f:
        templates = json.load(f)
        ans = f" Меню на день для {goal} \n\nЗавтрак: {templates[number]['brkf']}\n\nОбед: {templates[number]['lunch']}\n\nПолдник: {templates[number]['poldnik']}\n\nУжин: {templates[number]['dinner']}"
        return ans


def text_motivation() -> str:
    number = random.randint(0, 13)
    with open('motivation.json') as f:
            templates = json.load(f)
            ans = templates[number]['text']
            return ans

