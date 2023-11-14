
# the_oldest_customer = "Oleh" # Snake
# theOldestCustomr = "Oleh" # Camel case
# the-oldest-customer = "Oleh" # Kebab
# TheOldestCustomr = "Oleh" # Pascal

# function signature
# what in brackets = parameter
def welcome_mister(repetion): # <name of func> = welcome mister
    name = input("What is your name >>>") # oleh -> Oleh
    name = name.capitalize()
    print(f"Hello Mr. {name}")

for i in range(5):
    welcome_mister()

    ''' we do 4-10, not to do this:
    name = input("What is your name >>>") # oleh -> Oleh
    name = name.capitalize()
    print(f"Hello Mr. {name}")

    name = input("What is your name >>>") # oleh -> Oleh
    name = name.capitalize()
    print(f"Hello Mr. {name}")

    name = input("What is your name >>>") # oleh -> Oleh
    name = name.capitalize()
    print(f"Hello Mr. {name}")

    name = input("What is your name >>>") # oleh -> Oleh
    name = name.capitalize()
    print(f"Hello Mr. {name}")

    name = input("What is your name >>>") # oleh -> Oleh
    name = name.capitalize()
    print(f"Hello Mr. {name}")

    name = input("What is your name >>>") # oleh -> Oleh
    name = name.capitalize()
    print(f"Hello Mr. {name}")
''' 
def add (b, a=0):
    print(f"a {a}, b {b}")
    print (a+b)

add(1, 2)

def is_even(number):
    if number % 2 == 0:
        print(number, "is even")
        return True
    return False

res = is_even(4)
print(res)
