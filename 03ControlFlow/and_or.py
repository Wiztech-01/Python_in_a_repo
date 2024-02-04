"""
   working with the and and or operators
    and: both conditions must be true
    or: one of the conditions must be true
    or: not: negates the condition
   
   The following are the operators that we are going to work with
    1. and
    2. or
    3. not
    
    AND TABLE
    True and True = True
    True and False = False
    False and True = False
    False and False = False
    
    OR TABLE
    True or True = True
    True or False = True
    False or True = True
    False or False = False
    
    NOT TABLE
    not True = False
    not False = True
    
   
   A good way to learn this is by installing the ipython by using the following commands
    1. pip install ipython
    
    - once installled go to the terminal and type the following command
    1. ipython
    
    - from there you can now test the following commands
    1. True and True
    2. True and False
    3. False and True
    4. False and False
    5. True or True
    6. True or False
    7. False or True
    8. False or False
    9. not True
    10. not False
    11. not True and False
    12. not True or False
    13. not True and not False
    14. not True or not False
    15. not True and not True
    16. not True or not True
    17. not False and not False
    18. not False or not False
    19. not False and not True
    20. not False or not True
    21. not True and not True
    22. not True or not True
    23. not True and not False
    24. not True or not False
    25. not False and not False
  
   This will help you understand the and, or and not operators, especially when you are not sure on which one to use    
"""

userage: int = 17
country: str = "Kenya"

"""
   my first and operator
   
"""

if userage < 18 and country == "Kenya":
    #   both conditions must be true for the user to drink
    #  True and False = False
    # Here you can not drink
    print("You are not allowed to drink")
    
    # True and False = False
    # True and True = True
    # Here you can drink
elif userage >= 18 and country == "Kenya":
    print("You are now allowed to drink")

    # True and False = False
    # THe country is not Maku hence the path is false at this point
elif userage < 18 and country == "Maku":
    print("You can try looking if you can drink in Maku")
    
    
"""
    my first or operator
"""

userage: int = 17
country: str = "Maku"


if userage < 18 and country == "Kenya":
    #   both conditions must be true for the user to drink
    #  True and False = False
    # Here you can not drink
    print("You are not allowed to drink")
    
    # True and False = False
    # True and True = True
    # Here you can drink
elif userage >= 18 and country == "Kenya":
    print("You are now allowed to drink")

    # True or False = False
    # THe country is not Maku hence the path is false at this point
elif userage < 18 or country == "Maku":
    print("You can try looking if you can drink in Maku")