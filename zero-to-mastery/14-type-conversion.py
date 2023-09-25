#Lets say we have a facebook page with the info
name = "Jeremiah Bako"
age = 19
relationship_status = "single"

#Lets say my relationship status changes
relationship_status = "it's single"
print(relationship_status)

#ex2 

birth_year = input("what year were you born? ") #your birthyear is input as a str

age = 2023 - int(birth_year) #converting birth yeat to int
#we can also conver it to float

print(f"your age is: {age}")