"""
Параметри функцій можна встановлювати за замовчуванням. Вони присвоюються в першому рядку визначення функції:

def fun(a, b=2, c=3):
    return a + b * c
У цьому прикладі, якщо є тільки один обов'язковий параметр a при виклику функції fun, інші значення для локальних змінних b і c ми вказуємо відразу при визначенні функції.

Значення за замовчуванням можуть бути у будь-якої кількості параметрів. Але є важливий момент — параметри за замовчуванням повинні визначатися останніми у списку параметрів, тому що при виклику функції аргументи зіставляються з параметрами згідно з їхніми позиціями при оголошенні функції. Таким чином, у списку параметрів функції параметр зі значенням за замовчуванням не може знаходитись перед параметром без значення за замовчуванням.
"""
# Напишімо функцію, яка повертає повне ім'я користувача. У базі даних переважно зберігають ім'я користувача first_name, його прізвище last_name та по батькові, або, як заведено в західних країнах, друге ім'я — middle_name. Причому middle_name — це необов'язкова змінна, вона може бути, а може й не передаватися під час виклику функції. Наша функція повертатиме рядок з повним ім'ям 'first_name middle_name last_name', якщо ж змінна middle_name відсутня, то рядок, що повертається повинен бути 'first_name last_name'.

def get_fullname(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    
    return full_name

# Приклад виклику функції
first_name = 'John'
last_name = 'Doe'
middle_name = 'William'

# Варіант з middle_name
result_with_middle_name = get_fullname(first_name, last_name, middle_name)
print(f'Full Name (with middle name): {result_with_middle_name}')

# Варіант без middle_name
result_without_middle_name = get_fullname(first_name, last_name)
print(f'Full Name (without middle name): {result_without_middle_name}')
# Ця функція get_fullname приймає first_name, last_name і необов'язковий параметр middle_name. Якщо middle_name передається, то повертається повне ім'я, в іншому випадку повертається ім'я без middle_name.






