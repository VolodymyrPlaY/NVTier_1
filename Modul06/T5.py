"""
Додаток може виконати багато операцій між відкриттям та закриттям файлу. 
В будь-якому місці може статися помилка та додаток завершиться аварійно, 
не повернувши файловий дескриптор системі. Така поведінка, як вже згадувалося, 
небажана і може призводити до втрати даних.

Щоб уникнути цього, можна укласти блок коду, в якому відбувається робота з файлом, 
у блок try ... except:

fh = open('text.txt')
try:
    some_useful_function(fh)
except:
    print('An error has occurred!')
finally:
    fh.close()
В цьому прикладі ми викликали функцію some_useful_function всередині блоку try ... except і, 
якщо станеться виключення, то обов'язково виконається блок finally, в якому файл буде закритий. 
Цей підхід гарантує, що файловий дескриптор буде обов'язково повернений системі.

Але такий підхід не надто елегантний та читабельний.

Для покращення читабельності коду при збереженні 
функціоналу можна скористатися менеджером контексту open. 
Менеджер контексту — це синтаксична конструкція, яка покращує читабельність коду, 
але не вносить ніякого додаткового функціоналу.

with open('text.txt', 'w+') as fh:
    some_useful_function(fh)
Менеджер контексту складається з ключового слова with, після якого викликається сам менеджер і, 
якщо щось треба повернути з менеджера, то це щось можна передати у змінну, 
оголошену після ключового слова as. Далі ставиться двокрапка і блок коду, 
який буде виконаний всередині менеджера. У прикладі з try ... finally — це код, 
який йде всередині блоку try. Коли код виконається, менеджер контексту виконає те, 
що повинен зробити в будь-якому випадку, закрити файл наприклад (це те, що відбуваєтья в блоку finally).

Менеджер контексту open синтаксично повністю повторює свого класичного тезка open, 
вони повністю ідентичні з точки зору використання.

З точки зору роботи цей приклад робить у точності теж саме, 
що і попередній з блоком try ... finally. Але замість п'яти рядків коду, ви можете написати два, 
і код виглядає більш читабельним.

Такий спосіб роботи з файлами є рекомендованим у Python, оскільки гарантує, 
що програміст не забуде закрити файл у будь-якому разі.

"""
'''
Ми маємо таку структуру файлу:

60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
Кожен запис складається з трьох частин і починається з нового рядка. 
Наприклад, для першого запису початок 60b90c1c13067a15887e1ae1 — це первинний ключ бази даних MongoDB. 
Він завжди містить 12 байтів або рівно 24 символи. Далі ми бачимо прізвисько кота Tayson та його вік 3. 
Всі частини запису розділені символом кома ,

Розробіть функцію get_cats_info(path), яка повертатиме список словників із даними котів у вигляді:

[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
Параметри функції:

path - шлях до файлу
Вимоги:

прочитайте вміст файлу за допомогою режиму "r".
ми використовуємо менеджер контексту with
поверніть із функції список котів із файлу у потрібному форматі

STARTING CODE:

def get_cats_info(path):
  
'''
def get_cats_info(path):
    # Ініціалізуємо список для зберігання інформації про котів у вигляді словників
    cats_info = []
    
    # Відкриваємо файл за вказаним шляхом для читання за допомогою менеджера контексту with
    with open(path, 'r') as file:
        # Цикл для читання рядків файлу
        for line in file:
            # Розділяємо рядок на частини за допомогою коми
            parts = line.strip().split(',')
            
            # Створюємо словник із даними кота та додаємо його до списку
            cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]}
            cats_info.append(cat_info)
    
    # Повертаємо список із словниками про котів
    return cats_info

# Приклад виклику функції
path_to_file = 'path/to/your/cats_file.txt'  # Замініть це на шлях до вашого файлу
result = get_cats_info(path_to_file)
print(result)
#   Ця функція get_cats_info використовує менеджер контексту with для відкриття файлу та 
#   автоматичного його закриття. Вона читає рядок за рядком і розбиває кожен рядок на частини 
#   за допомогою коми. Потім створює словник із даними кота та додає його до загального списку. 
#   На кінці повертає список із словниками про котів у потрібному форматі. 
#   Зверніть увагу, що у цьому випадку використовується менеджер контексту with.