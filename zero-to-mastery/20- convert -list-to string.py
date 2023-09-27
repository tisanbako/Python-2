#we can combine a list to a string by using the join method
sentence = ""
sentence.join(["hi", "my", "name", "is", "Tisan"]) #this will give is black space
print(sentence)

#to achieve this we need to give create a new variable to convert the list to string

quote = ""
quote2 = quote.join(["work", "hard", "and", "you", "see"])
print(quote2)

#if we add a space between the quotation mark for the value of quote
#it returns a proper sentence
#Try it
quote3 = " "
quote4 = quote3.join(["work", "hard", "and", "you", "see"])
print(quote4)

#you can achieve this also by just remiving the the first variabe 
#and just start with the quotation marks

quote5 = " ".join(["work", "hard", "and", "you", "see"])
print(quote5)








#