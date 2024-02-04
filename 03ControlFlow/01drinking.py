"""
    This is a simple program to check if the user is allowed to drink
    The program will then check if the user is allowed to drink
    The program will then output the result
"""


##My first case

userage: int = 13

"""
  Starting with the if and Else 
  when the user is younger than 18, the user is not allowed to drink
"""
if userage < 18:
    print("You are not allowed to drink")

else:
    print("You are allowed to drink")
    


##My second case
userage: int = 20

"""
  Starting with the if and Else 
  when the user is oder  than 18, the user is allowed to drink
"""
if userage < 18:
    print("You are not allowed to drink")

else:
    print("You are allowed to drink")
    
    
##My third case

"""
    we are now going to work with the if elif and else
"""

userage: int = 26

if userage < 18:
    print("You are not allowed to drink")

elif userage >= 25:
    print("Stop wasting time drinking go get a job")

else:
    print("You are allowed to drink")