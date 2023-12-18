""" ЗАВДАННЯ: ПЕРЕВІРКА ПРЕФІКСА РЯДКА """
'''
У модулі роботи з функціями ми писали функцію get_fullname для складання повного імені користувача. 
Виконаємо невелике продовження для цього завдання та напишемо функцію is_check_name, 
яка приймає два параметри (fullname, first_name) і повертає логічне значення True або False. 
Це результат перевірки, чи є рядок first_name префіксом рядка fullname. 
Функція is_check_name чутлива до регістру літер, тобто "Sam" і "sam" для неї різні імена.
'''
# Ось функція is_check_name, яка перевіряє, чи є рядок first_name префіксом рядка fullname:

def is_check_name(fullname, first_name):
    # Перевірка, чи є first_name префіксом fullname
    return fullname.startswith(first_name)

# Приклад використання
fullname_example = "John Doe"
first_name_example = "John"

result = is_check_name(fullname_example, first_name_example)
print(result)  # Виведе True
# Ця функція використовує метод startswith, який повертає True, якщо рядок починається з вказаного префіксу, і False в іншому випадку. Функція is_check_name чутлива до регістру літер, тобто "Sam" і "sam" вважаються різними іменами.





