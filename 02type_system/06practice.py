"""
1. Create a variable called myclient and assign it the value "festus"
2. Create a variable called pizza_make and assign it the value "Thick"
3. Create a variable called pizza_size and assign it the value 14
4. Create a variable called pizza_additions and assign it the value "pepperoni"
5. Create a variable called extra_ingridients and assign it the value True
6. Create a variable called the_price and assign it the value 14.99

"""

myclient: str = "festus"
pizza_make: str = "Thick"
pizza_size: int = 14
pizza_additions: str = "pepperoni"
extra_ingridients: bool = True
the_price: float = 14.99

"""
    first way to print the work
"""

print(f"Hello {myclient}! Your pizza is ready")
print(f"The pizza is {pizza_make}")
print(f"The pizza size is {pizza_size}")
print(f"The pizza additions are {pizza_additions}")
print(f"Extra ingridients are {extra_ingridients}")
print(f"The price of the pizza is {the_price}")

"""
    second way to print the work using the format 
    
"""

the_whole_details: str = f"""
    Hello {myclient}! Your pizza is ready
    The pizza is {pizza_make}
    The pizza size is {pizza_size}
    The pizza additions are {pizza_additions}
    Extra ingridients are {extra_ingridients}
    The price of the pizza is {the_price}
"""

print(the_whole_details)