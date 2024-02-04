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
    
   
   
"""

userage: int = 17
country: str = "Kenya"

"""
   my first and and or operator
   
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