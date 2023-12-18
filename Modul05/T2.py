"""
Ми вже працювали з методами рядків на попередніх етапах. Розглянемо нову порцію методів, 
які стануть нам у пригоді.

Пошук у рядку
Метод find приймає три аргументи.

message = "Hello my little friend!"

print(message.find("li", 5, 15))  # 9
print(message.find("li", 10, 15))  # -1
print(message.find("li"))  # 9
Перший аргумент — підрядок, який шукатиме метод find в рядку message, 
другий аргумент — індекс початку пошуку в message, а третій — індекс закінчення пошуку. 
Якщо не вказати другий та третій аргумент, то пошук здійсниться по всьому рядку. 
Метод повертає індекс початку першого збігу у рядку та повертає -1, якщо послідовність не знайдено.

Є аналогічний метод пошуку підрядка в рядку - index. Основна відмінність полягає в тому, 
що якщо index не знайде підрядок, то викличе виключення ValueError.

message = "Hello my little friend!"

print(message.index("li", 5, 15))
print(message.index("li", 10, 15))
Вивід:

9
Traceback (most recent call last):
  File "e:\WebDir\Works\Python\python-homework-tracks\module-05\src\test.py", line 4, in <module>
    print(message.index("li", 10, 15))
ValueError: substring not found
Якщо вам треба провести пошук підрядка в рядку праворуч, існують методи rfind та rindex:

message = "Hello my little friend!"

print(message.rfind("li"))  # 9
print(message.rindex("li"))  # 9
Розбиття рядка на підрядки
Часто виникає ситуація, коли необхідно розбити рядок на підрядки за деяким символом, 
наприклад, розбити текст речення по пробілу після точки, або речення за словами. 
Для цього треба скористатися методом split, який приймає аргумент підрядок-маркер, 
який буде межею, за якою рядок буде розбитий на частини. 
В результаті роботи методу повертається список рядків.

message = "Hello, my little friend. Today is a very good day."
words = message.split(" ")
sentences = message.split(". ")
print(words)
print(sentences)
Вивід:

['Hello,', 'my', 'little', 'friend.', 'Today', 'is', 'a', 'very', 'good', 'day.']
['Hello, my little friend', 'Today is a very good day.']
Конкатенація рядків
Всі рядки незмінні, тому всі методи, які якось "модифікують" рядки, повертають нові рядки, 
ніяк не змінюючи оригінальний рядок.

Для об'єднання кількох рядків в один через деякий роздільник використовується метод join. 
По суті це операція зворотна split:

words = [
    "Hello,",
    "my",
    "little",
    "friend.",
    "Today",
    "is",
    "a",
    "very",
    "good",
    "day.",
]
sentences = ["Hello, my little friend", "Today is a very good day."]

message_from_words = " ".join(words)
message_from_sentences = ". ".join(sentences)

print(message_from_words)  # Hello, my little friend. Today is a very good day.
print(message_from_sentences)  # Hello, my little friend. Today is a very good day.
Заміна підрядка
Коли нам треба замінити деякий підрядок у рядку ми можемо скористатися методом replace:

message = "У темній кімнаті всі кішки чорні (мабуть)"
square_brackets = message.replace("(", "[").replace(")", "]")
clear_brackets = message.replace("(", "").replace(")", "")

print(square_brackets)  # У темній кімнаті всі кішки чорні [мабуть]
print(clear_brackets)  # У темній кімнаті всі кішки чорні мабуть
Для видалення фіксованої послідовності на початку рядка є метод removeprefix:

print('TestHook'.removeprefix('Test'))  # Hook
print('TestHook'.removeprefix('Hook'))  # TestHook
Є парний метод для видалення послідовності в кінці рядка, removesuffix:

print('TestHook'.removesuffix('Hook'))  # Test
print('TestHook'.removesuffix('Test'))  # TestHook

"""
'''
Ваша компанія веде блог. Треба реалізувати функцію find_articles для пошуку за статтями цього блогу. 
Є список articles_dict, в якому міститься опис статей блогу. 
Кожен елемент цього списку є словником з наступними ключами: прізвища авторів - ключ 'author', 
назва статті - ключ 'title', рік видання - ключ 'year'.

Реалізуйте функцію find_articles,

Параметр key функції визначає поєднання букв для пошуку. 
Наприклад, при key="Python" функція шукає, чи є у списку articles_dict статті, 
у назві чи іменах авторів яких зустрічається це поєднання літер. 
Якщо такі елементи списку були знайдені, треба повернути новий список зі словників, 
що містять прізвища авторів, назву та рік видання всіх таких статей.

Другий ключовий параметр функції letter_case визначає, 
чи треба враховувати під час пошуку регістр літер. 
За умовчанням він дорівнює False і регістр немає значення тобто пошук в тексті "Python" і "python" 
це те ж саме. Інакше потрібно шукати повний збіг.
'''
'''
STARTING CODE: 
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
'''    
"""    
def find_articles(key, letter_case=False):
    result_articles = []

    for article in articles_dict:
        author_name = article["author"]
        title = article["title"]

        if not letter_case:
            key = key.lower()
            author_name = author_name.lower()
            title = title.lower()

        if key in author_name or key in title:
            result_articles.append({
                "author": article["author"],
                "title": article["title"],
                "year": article["year"],
            })

    return result_articles

# Приклад використання
key_search = "ocean"
result = find_articles(key_search)
print(f"Статті, що містять '{key_search}' в імені автора чи назві:")
for article in result:
    print(f"Автор: {article['author']}, Назва: {article['title']}, Рік: {article['year']}")
# Ця функція шукає в списку articles_dict статті, в яких знаходиться вказане поєднання літер у назві чи імені автора. Параметр letter_case визначає, чи слід враховувати регістр літер під час пошуку. Повертає новий список статей, які відповідають критеріям пошуку.
"""


articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    result = []
    for i in articles_dict:
        print(i)
        title:str = i.get("title", "")
        author:str = i.get("author", "")
        if letter_case is False:
            title = title.lower()
            author = author.lower()
            key = key.lower()            
        if title.find(key) != -1:
            print(title,key)
            result.append(i)
        elif author.find(key) != -1:
            print(author, key)
            result.append(i)
    return result


answer = find_articles("Phyton", True)
print(answer)


""""    
    The code you provided is indeed correct and achieves the same functionality. It uses the find method on strings to check if the specified key is present in the title or author. Additionally, it includes a case-insensitive option by converting the strings to lowercase when the letter_case parameter is set to False.

    Here's a breakdown of the differences and improvements in the code you provided:

    Simplified Logic: Your code uses a simpler logic by directly using the find method on the title and author strings without creating additional variables.

    Print Statements: You added print statements to help debug and understand how the function is working, which can be useful for testing and troubleshooting.

    Parameter Naming: The parameters in your function (title, author, key) have clear names, making the code more readable.

    Overall, both versions of the code achieve the same goal. The choice between them depends on personal coding style preferences. Your version is clear and effective, and the print statements can be helpful during development. If you don't need the print statements, you can remove them for a cleaner final version.
""""




