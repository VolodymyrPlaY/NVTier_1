"""
Словник краще представляти як аналог адресної книги, в якій можна знайти адресу або контактну інформацію людини, знаючи лише його ім'я. Це називають зв'язком ключ (ім'я) — значення (інформація). Звідси випливає, що ключ повинен бути унікальним і в якості ключа повинні використовуватися тільки прості об'єкти, щоб за ними був можливий простий пошук.

Пари ключ-значення вказуються у словнику таким чином:

lang = {"Python": 1991, "Java": 1995, "JS": 1995}
Видно, що ключ і значення поділяються між собою двокрапкою, а пари значень, один від одного, відокремлюються комами, а потім все це розташовано у фігурних дужках.

Словники є екземплярами або об'єктами класу dict.

Щоб змінити або додати нове значення у словнику, використовується оператор присвоєння. Ім'я словника з ключем у квадратних дужках міститься ліворуч, а необхідне для цього ключа значення – праворуч. Якщо елемент із таким ключем вже існує у словнику, його значення буде перезаписано. В іншому випадку буде створено нову пару ключ-значення.

lang = {"Python": 1991, "Java": 1995}
lang["Java"] = 1991
lang["JS"] = 1995
print(lang)  # {"Python": 1991, "Java": 1991, "JS": 1995}
Розгляньмо деякі методи словників, що мають найчастіше використовування:

pop(key) — повертає значення елемента та видаляє пару ключ-значення зі словника
lang = {"Python": 1991, "Java": 1995}
result = lang.pop("Python")
print(result)  # 1991
print(lang)  # {"Java": 1995}
update(append_dict) — розширює словник значеннями з іншого словника:
lang = {"Python": 1991, "Java": 1995}
lang.update({"JS": 1995})
print(lang)  # {"Python": 1991, "Java": 1995, "JS": 1995}
clear() — очищує словник, не створюючи нового
lang = {"Python": 1991, "Java": 1995}
lang.clear()
print(lang)  # {}
copy() — повертає копію словника
lang = {"Python": 1991, "Java": 1995}
new_lang = lang.copy()
print(new_lang)  # {"Python": 1991, "Java": 1995}
print(lang)  # {"Python": 1991, "Java": 1995}
get(key[, default]) — не викликає винятку, якщо ключа немає у словнику, повертає default, за замовчуванням default=None.
lang = {"Python": 1991, "Java": 1995}
java = lang.get("Java", 1991)  # 1995
js = lang.get("JS", 1995)  # 1995
pascal = lang.get("Pascal")  # None
"""
'''
Сучасна система оцінок в університеті має такий вигляд:

Оцінка	Бали	Оцінка ECTS	Пояснення
1	0-34	F	Unsatisfactorily
2	35-59	FX	Unsatisfactorily
3	60-66	E	Enough
3	67-74	D	Satisfactorily
4	75-89	C	Good
5	90-95	В	Very good
5	96-100	A	Perfectly
Реалізуйте дві функції. Перша буде використовуватись у бухгалтерії при розрахунку стипендії, get_grade приймає ключ у вигляді оцінки ECTS, і має повертати відповідну п'ятибальну оцінку (перший стовпчик таблиці). Друга get_description теж приймає ключ у вигляді оцінки ECTS, але повертатиме пояснення оцінки в текстовому форматі (останній стовпчик таблиці) і буде використана в електронній заліковій книжці студента. На відсутній ключ функції повинні повертати значення None .
'''
# Ось реалізація двох функцій get_grade та get_description, які використовуються для отримання відповідно п'ятибальної оцінки та пояснення оцінки за ключем ECTS:


def get_grade(key):
    grade_mapping = {
        'F': 1,
        'FX': 2,
        'E': 3,
        'D': 3,
        'C': 4,
        'B': 5,
        'A': 5
    }
    return grade_mapping.get(key, None)

def get_description(key):
    description_mapping = {
        'F': 'Unsatisfactorily',
        'FX': 'Unsatisfactorily',
        'E': 'Enough',
        'D': 'Satisfactorily',
        'C': 'Good',
        'B': 'Very good',
        'A': 'Perfectly'
    }
    return description_mapping.get(key, None)

# Приклад використання:
ects_grade = 'B'
grade_result = get_grade(ects_grade)
description_result = get_description(ects_grade)

if grade_result is not None and description_result is not None:
    print(f'ECTS Grade: {ects_grade}\nNumeric Grade: {grade_result}\nDescription: {description_result}')
else:
    print(f'ECTS Grade {ects_grade} not found.')
# Ці функції використовують словники для відображення ключів ECTS на відповідні п'ятибальні оцінки та пояснення. Якщо ключ не знайдено, функції повертають None.
        
        
    
    