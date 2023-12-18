"""
РОБОТА З ДВОМА ФАЙЛАМИ
"""
'''
Розробіть функцію sanitize_file(source, output), що переписує у 
текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:

прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, 
використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write

STARTING CODE:

def sanitize_file(source, output):

'''
'''
def sanitize_file(source, output):
    # Відкриваємо вихідний файл для запису з використанням менеджера контексту with
    with open(output, 'w') as output_file:
        # Відкриваємо вхідний файл для читання з використанням менеджера контексту with
        with open(source, 'r') as source_file:
            # Читаємо рядок за рядком з вхідного файлу
            for line in source_file:
                # Очищаємо рядок від цифр і записуємо його у вихідний файл
                cleaned_line = ''.join(char for char in line if not char.isdigit())
                output_file.write(cleaned_line)

# Приклад виклику функції
source_path = 'path/to/your/source_file.txt'  # Замініть це на шлях до вашого вхідного файлу
output_path = 'path/to/your/output_file.txt'  # Замініть це на шлях до вашого вихідного файлу
sanitize_file(source_path, output_path)
Ця функція sanitize_file використовує два менеджери контексту with. 
Перший відкриває вихідний файл для запису, а другий відкриває вхідний файл для читання. 
Далі, за допомогою циклу, читає рядок за рядком з вхідного файлу, 
очищає його від цифр та записує у вихідний файл. 
Зверніть увагу, що ви можете замінити шляхи до файлів на свої.
'''
#   Функція open повинна бути викликана з аргументами source і 'r'
def sanitize_file(source, output):
    # Відкриваємо вхідний файл для читання з використанням менеджера контексту with
    with open(source, 'r') as source_file:
        # Читаємо вміст вхідного файлу
        content = source_file.read()
        
        # Очищаємо вміст від цифр
        cleaned_content = ''.join(char for char in content if not char.isdigit())
        
        # Відкриваємо вихідний файл для запису з використанням менеджера контексту with
        with open(output, 'w') as output_file:
            # Записуємо очищений вміст у вихідний файл
            output_file.write(cleaned_content)
'''
# Приклад виклику функції
source_path = 'path/to/your/source_file.txt'  # Замініть це на шлях до вашого вхідного файлу
output_path = 'path/to/your/output_file.txt'  # Замініть це на шлях до вашого вихідного файлу
sanitize_file(source_path, output_path)
Ця модифікована версія функції викликає функцію open з аргументами source і 'r', як ви вказали. 
Крім того, вона читає вміст вхідного файлу за допомогою методу read, 
очищує його від цифр та записує у вихідний файл. 
Знову ж таки, замініть шляхи до файлів на свої.
'''