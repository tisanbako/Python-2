#built in function and built in methods are kind of thesame but 
#built in methods are owned by something
#methods starts with a dot eg .append() .capitalize() .slit() 
#while gunctions can be len() round() range() type() print() input() int() str()
#function comes before the variable and methods come after the variable

name = "benjamin"
print(len(name)) #function
print(name.capitalize()) #method

#FUNCTION

print(len("hellllloooo"))
print(input("what is your name"))

greet = "hellloooo"
print(greet[:]) #hellloooo
print(greet[0:len(greet)]) #hellloooo
print(greet[0:9]) #slicing

#METHODS
quote = "to god be the glory"
print(quote.upper()) #print everything in uppercase (TO GOD BE THE GLORY)
print(quote.capitalize()) #to capitalize the first word (To god be the glory)
print(quote.lower())
print(quote.find("be")) #check if there's be and the index
print(quote.replace("be", "i give all")) #replace be with i give all


#All these 5 lines above are not variables, they arejust creating a new stings but we are not assigning it to a variable
#that way, we still have the value of quote to be (to god be the glory)

print(quote) #(to god be the glory)despite all the function or method the value of
#quote didnt change because strings are immutable we can't change. we can either them
# if we want to change the value of quote, we have to overite with a new value for quote eg
#quote = "my god is good"  

#we can change the value of quote or assign a new value we can
# do it in many ways eg

quote = "my new quote"
print(quote)

quote = quote.upper()
print(quote)