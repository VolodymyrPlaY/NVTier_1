"""
ЧИТАННЯ БІНАРНИХ ФАЙЛІВ У PYTHON
"""
'''
Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, 
створеного в попередньому завданню, де:

path – шлях до файлу.
Формат файлу:

andry:uyro18890D
steve:oppjM13LL9e
Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу та 
поверніть його з функції get_credentials_users у наступному форматі:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Вимоги:

Використовуйте менеджер контексту для читання з файлу

STARTING CODE:

def get_credentials_users(path):
    

'''
def get_credentials_users(path):
    credentials_list = []
    with open(path, 'rb') as file:
        for line in file:
            # Конвертуємо байти у рядок та додаємо до списку
            credentials_list.append(line.decode('utf-8').strip())
    return credentials_list

'''
# Приклад виклику функції
credentials = get_credentials_users('credentials.txt')
print(credentials)
У цьому прикладі функція get_credentials_users відкриває файл для читання в бінарному режимі ('rb'). Для кожного рядка файлу конвертується з байтів у рядок за допомогою методу decode('utf-8') та додається до списку credentials_list. Замініть значення змінної path на ваш реальний шлях до файлу.

'''