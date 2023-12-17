# 2 Modul
'''
a = input('Введіть число')
a = int(a)
if a > 0:
    print('Число додатне ')
elif a == 1:
    print('Число дорівнює 1')
else:
    print("a <= 0")
'''


# HW2 
# 2.1/15
"""
some_data = None
msg = some_data or "Не було повернено даних"

x = int(input("X: "))
y = 3

if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

result = y / x
print (result)

x = int(input("X: "))
y = 2

if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

    if x == 0:
        print("X can`t be equal to zero")
        x = int(input("X: "))

        if x == 0:
            print("X can`t be equal to zero")
            x = int(input("X: "))

result = y / x
print (result)

fruit = 'apple'
for char in fruit:
    print(char)


# 2.2/15

is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")

is_active = bool(is_active)
is_admin = bool(is_admin)
is_permission = bool(is_permission)

access = bool(is_admin) or (bool(is_active) and bool(is_permission))

# 2.3/15

work_experience = int(input("Enter your full work experience in years: "))

if work_experience >= 2 and work_experience <= 4:
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
else :
    developer_type = "Senior"

print(developer_type)

work_experience = int(input("Enter your full work experience in years: "))

if work_experience <= 1:
    developer_type = "Junior"
elif 1 < work_experience <= 5:
    developer_type = "Middle"
else:
    developer_type = "Senior"

print("Developer type:", developer_type)

# 2.3/15

num = int(input("Enter a number: "))

if num > 0:
    if num % 3
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"

# 2.7/15
num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num > 0:
    sum += num
    num -= 1
print(sum)

num = int(input("Enter the integer (0 to 100): "))
sum = 0
current_num = 1  # Initialize a variable to keep track of the current number in the loop

while current_num <= num:
    sum += current_num
    current_num += 1  # Increment the current number for the next iteration

print("The sum of numbers from 1 to", num, "is:", sum)

# 2.7/15

num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    repeat = int(input("Enter integar to add to sum? "))
    for i in range(repeat):
        sum = sum + num
    print(sum) 
    num = int(input("Enter integer (0 for output): "))
"""
# 2.11/15
while True:
    num = int(input("Введіть число (0 для виходу): "))
    if num == 0:
        break
    repeat = int(input("Скільки разів помножити число на 2? "))
    for i in range(repeat):
        num = num * 2
    print(num)