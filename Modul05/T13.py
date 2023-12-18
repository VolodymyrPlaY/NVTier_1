"""
ЗАВДАННЯ: ПОШУК EMAIL
"""
'''
Тепер ми потренуємося писати корисні регулярні вирази. 
Напишіть регулярний вираз для функції find_all_emails, 
яка буде в тексті (параметр text) знаходити всі email та повертати список отриманих з тексту збігів.

З метою спрощення приймемо, що:
    ми використовуємо для email, — англійський алфавіт
    префікс (все, що знаходиться до символу @) починається з латинської літери та 
        може містити будь-яке число або букву, включаючи нижнє підкреслення та символ точки. 
        Має складатися мінімум із двох символів
    суфікс email (все, що знаходиться після символу @) складається лише з букв англійського алфавіту, 
        та має дві частини, розділені точкою, також доменне ім'я верхнього рівня не може бути менш ніж 
        два символи (все, що після точки)
Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів email.

При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок 
регулярних виразів regex101.

STARTING CODE: 
import re


def find_all_emails(text):
    result = re.findall(r"", text)
    return result
'''
'''
import re

def find_all_emails(text):
    # Regular expression pattern for matching emails
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')

    # Find all matches in the text
    result = email_pattern.findall(text)

    return result

# Test the function
sample_text = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"
emails = find_all_emails(sample_text)
print(emails)
Now, the regular expression pattern is adjusted to correctly match the email addresses in 
the provided sample text. The test case should produce the expected result.

Should be:
r'\b[a-zA-Z][\w.]+@\w+\.[a-z]{2,}\b|[a-zA-Z][\w.]+@\w+\.[a-z]{2,}\b'

Proposed regular expression pattern seems to be a more inclusive version for matching email addresses. 
It allows for a wider range of characters in the local part of the email address, 
including uppercase letters and underscores. Here's the modified find_all_emails function using 
your suggested pattern:
'''
import re

def find_all_emails(text):
    # Regular expression pattern for matching emails
    email_pattern = re.compile(r'\b[a-zA-Z][\w.]+@\w+\.[a-z]{2,}\b|[a-zA-Z][\w.]+@\w+\.[a-z]{2,}\b')

    # Find all matches in the text
    result = email_pattern.findall(text)

    return result

# Test the function
sample_text = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"
emails = find_all_emails(sample_text)
print(emails)
#   This should cover a broader range of valid email address formats. 
#   Please feel free to test it with various email address patterns to ensure it meets your requirements.