"""
ЗАВДАННЯ: СТРУКТУРУЄМО ЗАПИС У ФАЙЛ

"""
'''
Задано відомість абітурієнтів, які склали вступні іспити до університету. 
Структура даних щодо абітурієнтів подана у вигляді наступного списку:

[
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
У кожному словнику цього списку записано прізвище абітурієнта — ключ name, код спеціальності, 
на яку він поступив — ключ specialty, та отримані ним бали з окремих дисциплін — ключі math (математика), 
lang ( українська мова) та eng (англійська мова)

Розробіть функцію save_applicant_data(source, output), 
яка буде вказаний список із параметра source зберігати у файл із параметра output

Структура файлу для зберігання повинна бути наступною. 
У кожному новому рядку файлу повинні бути записані через кому без прогалин прізвище абітурієнта, 
код спеціальності, на яку він поступив, та отримані ним бали за окремими дисциплінами.

Kovalchuk Oleksiy,301,175,180,155
Ivanchuk Boryslav,101,135,150,165
Karpenko Dmitro,201,155,175,185
Вимоги:

відкрийте файл output для запису, використовуючи менеджер контексту with та режим w.
запис нового вмісту файлу output має бути або за допомогою методу writelines, 
або використовувати метод write

STARTING CODE:

def save_applicant_data(source, output):

'''
def save_applicant_data(source, output):
    # Відкриваємо файл для запису з використанням менеджера контексту with
    with open(output, 'w') as output_file:
        # Проходимося по кожному словнику в списку абітурієнтів
        for applicant in source:
            # Записуємо дані абітурієнта у файл
            output_file.write(f"{applicant['name']},{applicant['specialty']},{applicant['math']},{applicant['lang']},{applicant['eng']}\n")

'''
# Приклад виклику функції
applicants = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

output_file_path = 'path/to/your/output_file.txt'  # Замініть це на шлях до вашого вихідного файлу
save_applicant_data(applicants, output_file_path)
У цьому прикладі функція save_applicant_data відкриває файл для запису з використанням менеджера контексту та записує дані абітурієнтів у файл. Замініть шлях до вихідного файлу на свій.

'''




