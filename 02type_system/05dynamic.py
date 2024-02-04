# The following is more about the dynamic typing in python
# Trying to understand the dynamic typing in python

""" 
    Dynamic typing in python
    In python, the type of a variable is not explicitly declared.
    The type of a variable is determined at runtime.
    This is called dynamic typing.
    This means that you can reassign a variable to a different data type.
    This makes python very flexible in assigning data types; it differs from other languages that are statically typed.
    This is why python is called a dynamically typed language.
    The following is an example of dynamic typing in python
"""

container = "mangoes"
print(f"The container contains {container}")

container = 45
print(f"The container contains {container}")


""" 
   for beginners this can seem confusing but it is a very powerful feature of python
   for the following we are going to introduce type hinting in python
   `Type Hinting` - Optional Static Type checking in python the `Mypy` is a static type checker for python
   Type hinting is a feature that allows you to specify the type of a variable.
    This makes the code more readable and easier to understand.
    The following is an example of type hinting in python
    Hepls take care of some minor bugs that might occur in the code
"""

diet: str  = "Beans"
print(f"The diet contains {diet}")

# The value of the variable diet is changed to "greengrams"
# The type of the variable diet is still a string
diet = "greengrams"
print(f"The diet contains {diet}")

""" 
  the variable will now be changed from the string to an integer
    the type of the variable diet is now an integer
    this will raise an error, even though the program will run. THis concepts shows the power of type hinting in python 
    and still states how python is dynamic in nature
        DEspite the error, the program will still run
        To be able to see the error ensure you have installled mypy using `pip insttall mypy`
        steps to follow after installation:
        1. go to settings
        2. search for `mypy`
        3. click on the checkbox `mypy: Enabled`
        
        - With that done, you can now see the error in the code, despite the fact that the code will run
"""

diet = 45

print(f"The diet contains {diet}")

