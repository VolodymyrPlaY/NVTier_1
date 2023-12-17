"""
Насамперед будь-які змінні у списку параметрів функції та будь-які змінні, створені у функції командою привласнення (наприклад, b = 10), є локальними для цієї функції. Це означає, що якщо ми змінимо їх під час виконання функції, це ніяк не позначиться на інших змінних за межами цієї функції. У наступному прикладі змінні a та b є локальними:

def add_ten(a):
    b = 10
    return a + b


print(add_ten(6))  # 16
Але якщо є потреба змінювати змінну за межами функції? Тоді змінну треба оголосити глобальною перед її використанням, для чого використовується команда global. Наступний приклад демонструє різницю між локальними та глобальними змінними:

a = 5
b = 0


def fun():
    global a
    a = 10
    b = 2


fun()
print(a)  # 10
print(b)  # 0
У прикладі ми привласнюємо a значення 10 — це привласнення значення для глобальної змінної a, яка існує поза межами функції fun. Ми оголосили змінну a глобальною всередині fun, і коли після виконання функції fun() ми виводимо значення print(a), глобальна змінна вже зазнала зміни та міститиме значення 10, замість початкового значення 5.

Змінна b поводиться інакше — спочатку вона посилається на те саме значення, що і змінна b за межами fun, але в результаті привласнення b = 2 вона починає вказувати на нове значення, яке локально для функції fun.
"""

# Необхідно написати функцію, яка буде обчислювати суму за користування послугами таксі. Сума складається з базового тарифу 40 грн, та 10 грн за кожен кілометр поїздки. Напишіть функцію, яка приймає один параметр — відстань поїздки в кілометрах. Функція має повертати підсумкову суму оплати за послуги таксі дійсним числом. Також функція повинна змінювати глобальну змінну — лічильник total_trip після кожного виклику та збільшувати її на одиницю.

# Глобальний лічильник для відстеження кількості поїздок
total_trip = 0

def calculate_taxi_fare(distance):
    # Глобальне ключове слово вказує на те, що змінна total_trip має бути використана як глобальна
    global total_trip
    
    # Базовий тариф
    base_fare = 40
    
    # Тариф за кожен кілометр поїздки
    per_km_rate = 10
    
    # Розрахунок суми
    total_fare = base_fare + (distance * per_km_rate)
    
    # Збільшення лічильника поїздок
    total_trip += 1
    
    return total_fare

# Приклад виклику функції
distance_of_trip = 5  # припустима відстань в кілометрах
fare = calculate_taxi_fare(distance_of_trip)

print(f'Trip #{total_trip}: The total fare for a {distance_of_trip}-km trip is {fare} UAH')
#Ця функція calculate_taxi_fare приймає відстань поїздки в кілометрах, розраховує суму за послуги таксі і змінює глобальний лічильник total_trip.

base_rate = 40
price_per_km = 10
total_trip = 0

def calculate_trip_price(distance_km):
    # Declare total_trip as a global variable
    global total_trip
    
    # Calculate the total fare
    total_fare = base_rate + (distance_km * price_per_km)
    
    # Increment the total_trip counter
    total_trip += 1
    
    return total_fare

# Example usage
distance_of_trip = 5  # Assume the distance of the trip is 5 km
fare = calculate_trip_price(distance_of_trip)

print(f'Trip #{total_trip}: The total fare for a {distance_of_trip}-km trip is {fare} UAH')
#In this code, the calculate_trip_price function takes the distance_km as a parameter, calculates the total fare, increments the total_trip counter, and returns the total fare. The global variables base_rate and price_per_km are used within the function. The example usage demonstrates how to call the function and print the result.



