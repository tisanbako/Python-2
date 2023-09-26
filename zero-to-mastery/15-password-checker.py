username = input("what is your username? ")
password = input("what is your password? ")

print(f"{username}, your password, {password} is {len(password)} letters long.")
#output will be jay, your password, jays is 4 letters long


#with this our password is exposed the password and we dont want that. instead
#we want to print **** to represent our secret


username = input("what is your username: ") #username
password = input("what is your password: ") #password

password_length = len(password) #star times legth of the password above
hidden_password = "*" * (password_length) #to get the *** for the length
print(f"{username}, your password {hidden_password} is {password_length} letters long")

#pitput will be Jay, your password ************ is 12 letters long

#this was the password is not shown


