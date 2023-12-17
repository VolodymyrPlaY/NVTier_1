"""
Для впорядкованих контейнерів існує особливий синтаксис, щоб отримувати деякі послідовності елементів з контейнера.

Наприклад, необхідно отримати перші 5 букв рядка:

greeting = "Hello my little friend"
hello = greeting[0:5]
Змінна hello у цьому прикладі міститиме рядок ``Hello'`.

Синтаксис зрізу складається з трьох чисел, вказаних через двокрапку. Перше число — це індекс першого елемента, який треба взяти для зрізу. Друге число — це індекс, до якого (не включаючи його) брати елементи для нової послідовності. І третє, воно за замовчуванням дорівнює одиниці, — це крок, з яким треба брати елементи у нову послідовність.

Візьмімо список чисел від 1 до 10 і збережемо окремо парні, непарні та кратні 3.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]
odd_numbers — ми беремо числа, починаючи з індексу 0 до 10 з кроком у 2 (отримаємо [1, 3, 5, 7, 9])
even_numbers — ми беремо числа, починаючи з індексу 1 до 10 з кроком у 2 (отримаємо [2, 4, 6, 8, 10])
three_numbers — ми беремо числа, починаючи з індексу 2 до 10 з кроком у 3 (отримаємо [3, 6, 9])
Ви можете не вказувати початковий, кінцевий індекс чи крок, пропускаючи його. За замовчуванням Python візьме зріз від початку до останнього елемента з кроком 1.

Перепишемо попередній приклад у скороченому синтаксисі:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:10:3]

numbers_copy = numbers[:]
numbers_copy у цьому прикладі — це зріз, який бере всі елементи numbers від початку до кінця з кроком 1.

Увага
Важливо пам'ятати, що до зрізу не входить елемент з індексом, до якого треба брати елементи.

numbers = [0, 1, 2, 3]
first_three = numbers[0:3]  # [0, 1, 2]
У цьому прикладі елемент 3 з індексом 3 не увійде до first_three.

Цікаво
Отримати список `numbers` у зворотному порядку допоможе `numbers[::-1]`
"""
'''
Ми розробляємо кулінарний блог. І в рецептах, при написанні списку інгредієнтів, ми розділяємо їх комами, а перед останнім ставимо союз "and", як у прикладі нижче:

2 eggs, 1 liter sugar, 1 tsp salt and vinegar
Напишіть функцію format_ingredients, яка прийматиме на вхід список з інгредієнтів ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] та повертатиме рядок зібраний з його елементів в описаний вище спосіб. Ваша функція має вміти обробляти списки будь-якої довжини.
'''
def format_ingredients(items):
    # Перевірка, чи список не порожній
    if not items:
        return ""

    # Отримання останнього інгредієнта та решта списку
    last_item = items[-1]
    rest_items = items[:-1]

    # Формування рядка інгредієнтів
    if rest_items:
        formatted_ingredients = ", ".join(rest_items) + " and " + last_item
    else:
        formatted_ingredients = last_item

    return formatted_ingredients

# Приклад використання:
ingredients_list = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
result = format_ingredients(ingredients_list)
print("Форматовані інгредієнти:", result)
# Ця функція використовує метод join для об'єднання елементів списку через кому, додає "and" перед останнім елементом і повертає сформований рядок інгредієнтів. Якщо вихідний список порожній, функція повертає порожній рядок.
