# 1 Modul

name = ("Volodymyr") # My name
print (name)
age = 34 # My age
print (age)

s = "Hello world!"
s1 = "Hello "
s2 = "world!"
joined_string = s1 + s2
print (joined_string)

hello_string = f"Hello, {name}!"
print (hello_string)

a = True
b = False
age1 = 18
person1 = age1 >= 18
print (person1)
age2 = 15
person2 = age2 <= 18
print (person2)

age = input("How old are you? ")
age = int(age)

# HW1 
# 1.1
name = ("Volodymyr")
age = 34
# 1.2
rate = 1.68
value = 100
payment = rate * value
print (payment)
# 1.3 !, 1.4
rate = 1.68
# Given values for day and night meter readings
value_day = 100  # Replace with the actual day meter reading
value_night = 50  # Replace with the actual night meter reading
# Calculate day and night tariffs
rate_day = rate
rate_night = rate / 2
# Calculate the cost for day and night electricity consumption
cost_day = value_day * rate_day
cost_night = value_night * rate_night
# Calculate the total payment
payment = cost_day + cost_night
# 1.5, 1.6, 1.7
first_name = "Volodymyr"
last_name = "Plakhtyna"
full_name = first_name + ' ' + last_name
message = f"Dear {first_name}, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at {full_name}. We are looking forward to seeing you!"
print (message)
# 1.8 !
length = 2.75
width = 1.75
area = length * width
show = f"With width {width} and length {length} of the room, its area is equal to {area}."
print (show)
# 1.9
a = -2 + 3j
b = 4 + 2.1j
result = a + b
# 1.10 
import math

a = -2
b = 7
c = -6
D = b ** 2 - 4 * a * c 
x1 = (-b + D ** 0.5) / (2 * a)
x2 = (-b - D ** 0.5) / (2 * a)
# 1.11
is_active = True
is_delete = False 
# 1.12
name = "Volodymyr"
age = 34
is_active = True
subscription = None
# 1.13 !
length = "2.75"
width = "1.75"
area = float(length) * float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
# 1.14
import math

RADIUS = 6371.01

lat1 = math.radians(50.45)
lon1 = math.radians(30.523)
lat2 = math.radians(51.5072)
lon2 = math.radians(-0.1275)

distance = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
# 1.15
name = input("Your name?: ")
email = input("Enter your email: ")
age = int(input("Type your age: "))
height = float(input("Tell us your hieght: "))
is_active = True
# 1.16
length = float(input("Lenght: "))
width = float(input("Width: "))
area = length * width
# DONE