"""
ЗАВДАННЯ. ПРОЧИТАТИ ЗАПИСАНИЙ ФАЙЛ
"""

'''
У попередній задачі ми записали співробітників у файл у такому вигляді:

Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), яка читатиме дані з файлу та повертатиме список співробітників у вигляді:

['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. Його необхідно прибирати при додаванні прочитаного рядка до списку.

Вимоги:

прочитайте вміст файлу за допомогою режиму "r".
ми поки що не використовуємо менеджер контексту with
поверніть із функції список співробітників із файлу

STARTING OCDE:
def read_employees_from_file(path):
    
    
'''
def read_employees_from_file(path):
    # Відкриваємо файл за вказаним шляхом для читання
    file = open(path, 'r')
    
    # Ініціалізуємо список для зберігання даних про співробітників
    employees_list = []
    
    # Цикл для читання рядків файлу
    for line in file:
        # Додаємо прочитаний рядок до списку співробітників (без символу нового рядка)
        employees_list.append(line.strip())
    
    # Закриваємо файл
    file.close()
    
    # Повертаємо список співробітників
    return employees_list

# Приклад виклику функції
path_to_file = 'path/to/your/employees.txt'  # Замініть це на шлях до вашого файлу
result = read_employees_from_file(path_to_file)
print(result)
#   Ця функція read_employees_from_file відкриває текстовий файл за вказаним шляхом, 
#   читає його рядок за рядком, та додає прочитаний рядок (без символу нового рядка) 
#   до списку співробітників. Потім функція повертає цей список. 
#   Знову ж таки, зверніть увагу, що дана функція не використовує менеджер контексту with (для простоти).