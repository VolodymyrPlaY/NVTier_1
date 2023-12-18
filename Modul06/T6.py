"""
ЗАВДАННЯ - ШУКАЄМО РЕЦЕПТ
"""
'''
Нагадаємо, що у 4 модулі ми для кулінарного блогу писали функцію format_ingredients, яка приймала на вхід список з інгредієнтами рецепта.

Ми продовжимо працювати в цьому напрямку та створимо функцію, яка шукатиме рецепт у файлі та повертатиме знайдений рецепт у вигляді словника певної форми.

У вас є файл, який містить рецепти у вигляді:

60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil
60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon
60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce
60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese
60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water
Кожен рецепт записаний з нового рядка (не забуваємо під час вирішення завдання про кінець рядка). Кожен запис починається з первинного ключа бази даних MongoDB. Далі через кому, йде назва рецепта, а потім через кому, йде перелік інгредієнтів рецепта.

Вам необхідно реалізувати функцію, котра буде отримувати інформацію про рецепт у вигляді словника для кожної страви що шукається. Створіть функцію get_recipe(path, search_id), яка повертатиме словник для рецепта із зазначеним ідентифікатором MongoDB.

Де параметри функції:

path — шлях до файлу.
search_id — первинний ключ MongoDB для пошуку рецепта
Вимоги:

Використовуйте менеджер контексту with для читання з файлу
Якщо рецепта із зазначеним search_id у файлі немає, функція повинна повернути None
Приклад: для файлу, вказаного вище, виклик функції у вигляді

get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")
Повинен знайти у файлі рядок 60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese і повернути результат у вигляді словника такої структури:

{
    "id": "60b90c3b13067a15887e1ae4",
    "name": "Watermelon Cucumber Salad",
    "ingredients": [
        "1 large seedless watermelon",
        "12 leaves fresh mint",
        "1 cup crumbled feta cheese",
    ],
}

STARTING CODE:

def get_recipe(path, search_id):
    
    
'''
def get_recipe(path, search_id):
    # Відкриваємо файл за вказаним шляхом для читання за допомогою менеджера контексту with
    with open(path, 'r') as file:
        # Цикл для читання рядків файлу
        for line in file:
            # Розділяємо рядок на частини за допомогою коми
            parts = line.strip().split(',')
            
            # Перевіряємо, чи знайдено рецепт із зазначеним search_id
            if parts[0] == search_id:
                # Створюємо словник із даними рецепта та повертаємо його
                recipe = {"id": parts[0], "name": parts[1], "ingredients": parts[2:]}
                return recipe
    
    # Якщо рецепта із зазначеним search_id не знайдено, повертаємо None
    return None
'''
# Приклад виклику функції
path_to_file = 'path/to/your/recipes_file.txt'  # Замініть це на шлях до вашого файлу
recipe_id_to_search = '60b90c3b13067a15887e1ae4'
result = get_recipe(path_to_file, recipe_id_to_search)
print(result)
Ця функція get_recipe використовує менеджер контексту with для відкриття файлу та 
автоматичного його закриття. Вона читає рядок за рядком та перевіряє, 
чи зустрічається рецепт із зазначеним search_id. Якщо такий рецепт знайдено, 
то створює словник із даними рецепта та повертає його. 
Якщо рецепт із зазначеним search_id не знайдено, повертає None.
'''