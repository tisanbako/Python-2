print("hello")
print("hello Jerry")
name ="""Jeremiah
is a
boy"""

print(name) #

#we can write strings across more than one lines using three quatation marks
long_string = """
WOW
0 0
---
"""
print(long_string)

name = "jeremiah"
surname = "bako"
full_name = (name + surname)
print(full_name) #this won't print name with space. we can space the name in two ways

#1 spacing the value of the surname eg 
name = "jeremiah"
surname = " bako"
full_name = (name + surname)
print(full_name)

#or add a string with space " " on full name
name = "jeremiah"
surname = "bako"
print(f"your name is {name} {surname}") #my exp using format function

# print(full_name)

#STRING CONCATENATION
#this isused to merge two strings into a single object, you may use the + operator.
#like what we didi above with jeremiah bako

msg = "you look cute"
msg2 = "hmu"
#print(msg, msg2)  this will print it the values as two seperate entity.
#to make it one 
msg3 = (msg + " " + msg2)
print(msg3)

print("Tisan" + " Bako")

