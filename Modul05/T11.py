"""
Коли потрібно знайти всі відповідні шаблону значення, можна скористатися функцією findall.

s = "I bought 7 nuts for 6$ and 10 bolts for 3$."
numbers = re.findall('\d+', s)
print(numbers)  # ['7', '6', '10', '3']
findall — повертає список усіх відповідностей шаблону.

Складання регулярних виразів — це окрема велика тема гідна окремого вивчення. 
Регулярні вирази складаються з блоків та модифікаторів.

Прикладом блоку може бути:

. — будь-який символ, крім символу кінця рядка.
\d — число або [0-9].
\D — не число, або [^0-9].
\s — будь-який символ, що позначає пробіл або табуляцію, перенесення рядка та ін.
\w — будь-яке число або літера, включаючи нижнє підкреслення, або [a-zA-Z0-9_].
\W — не буква, не число і нижнє підкреслення.
\S — збігається із не пробільними символами.
\b — збіги шукатимуться лише на межах слів (на початку або в кінці).
\B — збіги шукатимуться тільки не на межах слів.
\n — збігається із символом переводу рядка.
Використовуючи квадратні дужки [a,b,c,z], Ви можете вказати групу символів, 
пошук яких потрібно зробити. 
Символ ^ перед групою символів у квадратних дужках [^a,b,c,z] говорить про те, 
що потрібно зробити пошук усіх символів алфавіту, крім заданих. 
Використовуючи тире (-) між символами у квадратних дужках [a-c, z], 
Ви можете встановити діапазон символів, пошук яких потрібно зробити.

import re

s = "I bought 77 nuts for 6$ and 110 bolts for 3$."

print(re.findall("[0,1,3,6,7]", s))
print(re.findall("[^0,1,3,6,7]", s))
Вивід:

['7', '7', '6', '1', '1', '0', '3']
['I', ' ', 'b', 'o', 'u', 'g', 'h', 't', ' ', ' ', 'n', 'u', 't', 's', ' ', 'f', 'o', 'r', ' ', '$', ' ', 'a', 'n', 'd', ' ', ' ', 'b', 'o', 'l', 't', 's', ' ', 'f', 'o', 'r', ' ', '$', '.']
Модифікатори можуть вказувати на число повторень блоку у виразі, наприклад:

? 0 або 1 раз
+ 1 або більше разів
* 0 або більше разів
{n} суворо n разів (n ціле число)
{n, m} від n до m разів
Використання круглих дужок:

Круглі дужки можуть бути використані для групування символів перед модифікаторами. 
Якщо встановити модифікатор після дужок, то він буде застосовуватися до всього вмісту дужок, 
а не одного символу.

import re

s = "I bought 77 nuts for 6$ and 110 bolts for 3$."

print(re.findall("(\d){3}", s))  # ['0']
print(re.findall("[\d]{3}", s))  # ['110']
Круглі дужки також використовуються для пошуку альтернатив.

import re

s = "I bought 77 nuts for 6$ and 110 bolts for 3$."

print(re.findall("(for|and)", s))  # ['for', 'and', 'for']
"""
'''
Для закріплення матеріалу напишіть функцію find_all_words, яка шукає збіг слова в тексті. 
Функція повертає список всіх знаходжень слова в параметрі word в тексті у вигляді будь-якого написання, 
тобто, наприклад, можливі варіанти написання слова "Python" як pYthoN, pythOn, PYTHOn і т.і. 
головне, щоб зберігався порядок слів, регістр не має значення.

Підказка: функції модуля re приймають ще ключовий параметр flags і 
ми можемо визначити нечутливість до регістру, надавши йому значення re.IGNORECASE

STARTING CODE:
import re


def find_all_words(text, word):
'''    
import re

def find_all_words(text, word):
    # Search for all occurrences of the word in a case-insensitive manner
    matches = re.finditer(fr'\b{re.escape(word)}\b', text, flags=re.IGNORECASE)

    # Extract the matched strings and return them in a list
    result_list = [match.group() for match in matches]

    return result_list

#   Test the function
'''
text = "Python is a popular programming language. Python is versatile and readable."
word_to_find = "python"
result = find_all_words(text, word_to_find)

print(result)
'''
#   This function uses re.finditer to find all occurrences of the word in the text 
#   in a case-insensitive manner. The result is then returned as a list of matched strings. 
#   In the provided example, the output will be:

#   ['Python', 'Python']
    