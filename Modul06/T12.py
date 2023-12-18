"""
У комп'ютерах всі дані різних типів передаються як одиниці та нулі. 
Однак деякі канали зв'язку та додатки не завжди можуть зрозуміти всі біти, які вони отримують.

Щоб обійти це обмеження, ви можете кодувати свої дані в текст, 
підвищуючи шанси на їхню правильну передачу та обробку. 
Base64 - популярний формат перетворення двійкових даних на символи ASCII, 
що широко використовується в більшості мереж та додатків.

Так, наприклад, зображення в HTML може виглядати так:

<img src="data:image/png;base64,aVRBOw0AKg1mL9..."/>
Це зображення у вигляді тексту

Тепер подивімося, як ми можемо використати в Python Base64 для кодування та декодування даних.

Python надає base64 модуль, який дозволяє легко кодувати та декодувати інформацію. 
Спочатку ми конвертуємо рядок у байтовий об'єкт. 
Після перетворення ми можемо використовувати base64 модуль для його кодування.

Приклад:

import base64

message = "Hello world!"
message_bytes = message.encode("utf-8")
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode("utf-8")

print(base64_message)  # SGVsbG8gd29ybGQh
У наведеному вище прикладі ми імпортували base64 модуль. 
Змінну message конвертуємо в байтовий об'єкт, використовуючи рядковий метод encode, 
і зберігаємо його в message_bytes. 
Потім ми кодуємо message_bytes та зберігаємо результат в base64_bytes, 
використовуючи base64.b64encode метод. Нарешті, ми отримуємо представлення перетворення Base64 у 
вигляді рядка, декодуючи змінну base64_bytes. В результаті змінна base64_message зберігатиме 
наступний рядок SGVsbG8gd29ybGQh

При Базовій аутентифікації пару username:password частіше всього кодують у Base64 форматі.

Якщо використовується схема авторизації «Базова», дані користувача формуються так:

Логін та пароль, розділені двокрапкою aladdin:opensesame.
Підсумковий рядок, закодований в Base64 YWxhZGRpbjpvcGVuc2VzYW1l.
Джерело
"""
'''
Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список, виконує кодування кожної пари username:password у формат Base64 та повертає список із закодованими парами username:password у вигляді:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']

STARTING CODE:

import base64


def encode_data_to_base64(data):

'''
'''
import base64

def encode_data_to_base64(data):
    encoded_data = []
    
    for entry in data:
        # Розділяємо username та password за допомогою ':'
        username, password = entry.split(':')
        
        # Кодуємо username та password в форматі Base64 та додаємо до списку
        encoded_username = base64.b64encode(username.encode('utf-8')).decode('utf-8')
        encoded_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
        
        encoded_entry = f'{encoded_username}:{encoded_password}'
        encoded_data.append(encoded_entry)
    
    return encoded_data

# Приклад виклику функції
credentials = ['andry:uyro18890D', 'steve:oppjM13LL9e']
encoded_credentials = encode_data_to_base64(credentials)
print(encoded_credentials)
#   У цьому прикладі функція encode_data_to_base64 перебирає кожний елемент у вхідному списку data, 
#   розділяє username та password, кодує їх в форматі Base64 та додає закодовану пару до 
#   нового списку encoded_data. Нарешті, новий список з закодованими парами повертається з функції.
'''
import base64

def encode_data_to_base64(data):
    encoded_data = []
    
    for entry in data:
        # Кодуємо кожен запис в форматі Base64 та додаємо до списку
        encoded_entry = base64.b64encode(entry.encode('utf-8')).decode('utf-8')
        encoded_data.append(encoded_entry)
    
    return encoded_data

'''
# Приклад виклику функції
credentials = ['andry:uyro18890D', 'steve:oppjM13LL9e']
encoded_credentials = encode_data_to_base64(credentials)
print(encoded_credentials)
Ця версія коду просто кодує кожен елемент списку у форматі Base64, як ви вказали.
'''