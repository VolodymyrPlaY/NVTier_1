# 2 Modul

a = input('Введіть число')
a = int(a)
if a > 0:
    print('Число додатне ')
elif a == 1:
    print('Число дорівнює 1')
else:
    print("a <= 0")



# HW2 
# 2.1
some_data = None
msg = some_data or "Не було повернено даних"

x = int(input("X: "))
y = int(input("Y: "))

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


# 2.2
is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
else :
    is_next = False
print (is_next)    
    
    