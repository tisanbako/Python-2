is_old_enough = False
is_licence = True 

if is_old_enough: # = True
    print("you are old enough to drive")
elif is_licence:
    print("you can drive now")

else:
    print("you're too young to drive")    

#What happens if someone has alicence and is not old enough, ot old enough but dont have a 
# license? so what we have about is not ideal we need a both licence and age to be True at same time

#modifying the variables for clean block

old_enough = True
has_licence = True

if old_enough and has_licence: #: means true
    print("you can drive now")
else:
    print("you are not of age")    

#Another way to do the if else logic is using Ternary Operator (Conditional expression)  
#This a shortcut and can be use for some if else statement..

#condition_if_true if condition else condition_if_else
#eg
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)     #change -s_friend to False and see