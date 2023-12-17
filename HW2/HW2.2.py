"""
    Технiчний опис завдань
    Завдання 1
    Доробіть консольного бота помічника та додайте обробку помилок.

    Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
    Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо. 
    Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.

    Додамо декоратор input_error для обробки помилки ValueError

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return "Give me name and phone please."

        return inner

    Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

    @input_error
    def add_contact(args, contacts):
        name, phone = args
        contacts[name] = phone
        return "Contact added."

    Вам треба додати обробники до інших команд, та додати в декоратор обробку винятків інших типів. Бажаємо успіху при виконані домашнього завдання.

"""


