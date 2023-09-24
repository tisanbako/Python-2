#Lets say we have a page and we want our users to see a hello message

user = "patrick" #this name can be gotten from thedata base

print("hello " + user)

#what if we get keeting more variables we want to add like age

age = 55 

print("hello " + user + "," + " " + "you are " + str(age) + " years old") #This is 
#concatination.. t
#The better way tp do this and make it less cumbasome withour conversion of 
#data types we use the formattes strings
#Now instead of ading + "" and calculating spaces, we just use f in the 
#begining with the variables in curlybraces eg
print(f"hello {user}. You are {age} years old" )