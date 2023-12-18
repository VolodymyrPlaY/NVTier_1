"""
Специфікація набагато складніший модифікатор. З її допомогою можна:
змінювати розрядність представлення цілих чисел (десяткові, вісімкові, шістнадцятиричні та ін.);
print('dec: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))  # dec: 15 hex: f bin: 1111
змінювати точність представлення дробових чисел (округлювати до вказаної кількості знаків);
print('pi: {:0.3}'.format(3.1415))  # pi: 3.14
як відображати знак чисел:
print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))  # "1" "+2" "-3" " 4"
як вирівняти положення елементу і чим (якими символами) доповнити;
print("|{:<10}|{:*^10}|{:>10}|".format('left', 'center', 'right'))  # |left      |**center**|     right|
Знання про цей інструмент не є критично важливим, але використання форматування рядків в 
домашній роботі для конструювання "красивішого" результату виконання скрипта, буде плюсом.
"""
'''
Попрацюємо трохи зі специфікацією у форматуванні рядків. 
Напишіть функцію formatted_numbers, яка повертає список відформатованих рядків, 
щоб під час виведення наступного коду:

for el in formatted_numbers():
    print(el)
Виходила наступна таблиця:

| decimal  |   hex    |  binary  |
|0         |    0     |         0|
|1         |    1     |         1|
|2         |    2     |        10|
|3         |    3     |        11|
|4         |    4     |       100|
|5         |    5     |       101|
|6         |    6     |       110|
|7         |    7     |       111|
|8         |    8     |      1000|
|9         |    9     |      1001|
|10        |    a     |      1010|
|11        |    b     |      1011|
|12        |    c     |      1100|
|13        |    d     |      1101|
|14        |    e     |      1110|
|15        |    f     |      1111|
всі стовпці мають ширину 10 символів
у заголовків таблиці вирівнювання по центру
перший стовпець десяткових чисел — вирівнювання по лівому краю
другий стовпець шістнадцяткових чисел — вирівнювання по центру
третій стовпець двійкових чисел — вирівнювання з правого краю
вертикальний символ | не входить у ширину стовпця
Як ви вже зрозуміли, функція formatted_numbers виводить таблицю чисел від 0 до 15 у десятковому, 
шістнадцятковому та бінарному форматі.
'''
'''
def formatted_numbers():
    formatted_list = []

    # Header
    header = "| decimal  |   hex    |  binary  |"
    formatted_list.append(header)

    # Separator line
    separator = "|" + "-" * 10 + "|" + "-" * 10 + "|" + "-" * 10 + "|"
    formatted_list.append(separator)

    # Data rows
    for i in range(16):
        decimal = "{:<10}".format(i)
        hex_value = "{:^10}".format(hex(i)[2:])
        binary = "{:>10}".format(bin(i)[2:])
        row = "|" + decimal + "|" + hex_value + "|" + binary + "|"
        formatted_list.append(row)

    return formatted_list

# Example usage
for el in formatted_numbers():
    print(el)
#   This should produce the desired table of formatted numbers. 
#   The formatted_numbers function generates and returns a list of strings,
#   where each string represents a row in the table. 
#   The print(el) loop is used to display each row of the table.
'''
def formatted_numbers():
    result = [
        f"|{'decimal':^10}|{'hex':^10}|{'binary':^10}|"
    ]
    for i in range(16):
        decimal = f"{i:<10}"
        hex_value = f"{hex(i)[2:]:^10}"
        binary = f"{bin(i)[2:]:>10}"
        result.append(f"|{decimal:^10}|{hex_value:^10}|{binary:^10}|")
    return result
# Перевірка:
for row in formatted_numbers():
    print(row)






