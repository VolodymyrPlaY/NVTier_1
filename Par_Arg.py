def show(name, age, gender="Male"): # gender basic parameter  
    print(f"{name=}")
    print(f"{age=}")
    print(f"{gender=}")

show("Bob", "20", "Male") # positional (позиційні)
show(age=30, name="Bill") # named (іменовані)