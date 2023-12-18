"""
До цього моменту ми використовували функцію findall. Результат виконання відповідає всім входженням шаблону, а не тільки першому, як, наприклад, у функції search.

Але якщо ми бажаємо отримати більше інформації про всі збіги шаблону, ніж список тексту від findall, необхідно використовувати finditer — це корисно, оскільки вона надає об'єкти збігів замість рядків.

re.finditer(pattern, string, flags=0)
Функція finditer повертає ітератор, що дає об'єкти збігів по всіх збігах, що не перекриваються для шаблону pattern у рядку string. Рядок сканується зліва направо, а збіги повертаються в тому порядку, в якому їх знайшли.

Найкраще — це показати на прикладі 13 завдання, знаходження email адрес.

import re

regex = r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}"

test_str = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"

matches = re.finditer(regex, test_str)

for match in matches:
    print(f"{match.group()} start: {match.start()} end: {match.end()}")
Результат виводу:

Ima.Fool@iana.org start: 0 end: 17
Fool@iana.org start: 35 end: 48
first_last@iana.org start: 49 end: 68
first.middle.last@iana.or start: 69 end: 94
abc111@test.com start: 106 end: 121
"""
'''
І останнє завдання на регулярні висловлювання — це пошук у тексті гіперпосилань.

Напишіть регулярний вираз для функції find_all_links, яка буде в тексті (параметр text) 
знаходити всі лінки та повертати список отриманих з тексту збігів.

З метою спрощення приймемо, що:

Початок гіперпосилання може бути http:// або https://
доменне ім'я — це набір латинських букв, цифр, символів підкреслення _ та точок .
символи точок . не можуть зустрічатися поруч
Фактично в навчальному прикладі ми шукатимемо прості url адреси:

https://www.google.com
https://www.facebook.com
https://github.com
Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів гіперпосилань.

При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для 
перевірок регулярних виразів regex101.

STARTING CODE:
import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"", text)
    for match in iterator:
        result.append(match.group())
    return result

'''
#   Ось регулярний вираз для функції find_all_links:


import re

def find_all_links(text):
    result = re.findall(r'https?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}', text)
    return result

#   Цей вираз шукає лінки, які починаються з http:// або https://, і мають доменне ім'я, 
#   що складається з латинських букв, цифр, символів підкреслення (_) та точок (.). 
#   Символи точок не можуть зустрічатися поруч.

#   Якщо у вас є ще які-небудь запитання або якщо щось потрібно додатково пояснити, 
#   не соромтеся питати!
