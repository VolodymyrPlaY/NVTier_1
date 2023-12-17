"""ЗАВДАННЯ: ВИПАДКОВИЙ НАДІЙНИЙ ПАРОЛЬ"""
'''
І, нарешті, третій, останній етап. Використовуючи рішення із попередніх двох завдань, напишіть функцію get_password, яка згенерує нам випадковий надійний пароль та поверне його. Алгоритм простий — ми генеруємо пароль за допомогою функції get_random_password і, якщо він проходить перевірку на надійність функцією is_valid_password, повертаємо його, якщо ні — повторюємо ітерацію знову.

Примітка: Хорошою практикою буде обмежити кількість спроб (наприклад, до 100), щоб не отримати нескінченний цикл.
'''

from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num


def get_password():
    max_attempts = 100
    attempts = 0
    while attempts < max_attempts:
        password_candidate = get_random_password()

        if is_valid_password(password_candidate):
            return password_candidate

        attempts += 1

    print("Failed to generate a reliable password within the limited attempts.")
    return None

generated_password = get_password()
print("Generated reliable password:", generated_password)    
    
#   Ця функція генерує пароль за допомогою get_random_password та перевіряє його на надійність за допомогою is_valid_password. Якщо пароль відповідає критеріям, він повертається. Якщо не вдається згенерувати надійний пароль протягом обмеженої кількості спроб, виводиться повідомлення і повертається None.
    
        
        
        
    