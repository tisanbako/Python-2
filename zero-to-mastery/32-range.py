#when looping in python, one of the most common tools used is range function
#Rance returns an object that produces a sequence of integers from start(inclusive)
#to stop (exclusive) by step
#Range creates a special kind of object that we can iterate over


print(range(100))    #range(0, 100)
print(range(0, 100))    #range(0, 100)

#but when we use it in a loop function to loop as many times as we want eg

for number in range(100):
    print(number)  #prints 0-100 as using range we are able to look 100 times
#this tell the loop how many times to run


for i in range(10):
    print("email, email list")    #this tells python to print attempt 10 times

for _ in range(0, 10, 2):
    print(_)            #this will give is 0 2 4 6 8 as we tell it to step over two places


for l in range(10, 0, -1):
    print(l)          #10 9 8 7 6 5 4 3 2 1

for l in range(10, 0, -2):
    print(l)             #10 8 6 4 2

#We can also use range wrapped in a list eg 

print(list(range(10)))    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for r in range(2):
    print(list(range(10)))   #this is saying print 0-9 and convert to list twice
  

