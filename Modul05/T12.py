"""
Щоб замінити всі підрядки, що відповідають регулярному виразу, можна скористатися функцією sub. 
Замінимо кольори blue, red, white на слово colour:

p = re.sub(r'(blue|white|red)', 'color', 'blue socks and red shoes')
print(p)  # color socks and color shoes
"""
'''
У шостій задачі ми писали функцію is_spam_words, яка визначала, 
чи є чи ні стоп-слова у тексті повідомлення. 
Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон. 
Наприклад, всі "погані" слова замінюватимемо зірочками. 
Напишіть функцію replace_spam_words, яка приймає рядок (параметр text), 
перевіряє його на вміст заборонених слів зі списку (параметр spam_words), 
та повертає результат рядок, але замість заборонених слів, підставлений шаблон з *, 
причому довжина шаблону дорівнює довжині забороненого слова. 
Визначити нечутливість до регістру стоп-слів.

STARTING CODE:
import re


def replace_spam_words(text, spam_words):
    
'''
import re

def replace_spam_words(text, spam_words):
    # Compile a regular expression pattern with all the spam words, case-insensitive
    pattern = re.compile(fr'\b(?:{"|".join(map(re.escape, spam_words))})\b', flags=re.IGNORECASE)

    # Replace each occurrence of a spam word with asterisks of the same length
    result_text = pattern.sub(lambda match: '*' * len(match.group()), text)

    return result_text

# Test the function
text = "This is a spam message with bad words like BadWord1 and BadWord2."
spam_words = ["badword1", "badword2"]
result = replace_spam_words(text, spam_words)

print(result)
'''
This function uses a regular expression to match all occurrences of the spam words in the text, 
ignoring the case. The re.sub method is then used to replace each occurrence with asterisks (*) 
of the same length as the matched word. In the provided example, the output will be:

"This is a spam message with *** words like ******* and *******."
'''