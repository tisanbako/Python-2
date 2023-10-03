#Lets say we have a page and we want our users to see a hello message

user = "patrick" #this name can be gotten from the database in real work place

print("hello " + user)

#what if we get getting more variables we want to add like age

age = 55 


print("hello " + user + "," + " " + "you are " + str(age) + " years old") #This is 
#concatination.. t
#The better way tp do this and make it less cumbasome withour conversion of 
#data types we use the formattes strings
#Now instead of ading + "" and calculating spaces, we just use f in the 
#begining with the variables in curlybraces eg
print(f"hello {user}. You are {age} years old" )
#unlike concactination, this is short and clean, no + or "" 
# trying to find space 


#FORMATTING FLOATS WITH DECIMAL PLACES

price = 49
print(f"You can get it for only {price:.2f} dollars!")
#here price: This is the variable or value that you want to insert into the string.
#: The colon is used to indicate that you are specifying a format.
#.2f This is a format specification. It means that you want to format 
#price as a floating-point number with 2 decimal places (hence the 2 after the dot).



#For example, if price is 19.99, using 
# {price:.2f} in a string will result in "19.99".
price = 19.99
# formatted_price = f"The price is {price:.2f} dollars."
# print(formatted_price)
print(f"the price is {price}") #for consstecy ypu can use {price:.2} it 
#will return thesame value
