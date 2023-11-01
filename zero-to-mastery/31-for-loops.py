#for loops allow us to iterate on anything that has a collection of items
#Iterables simply means an object that can be iterated over (looped). this could be a str, list
#dict, tuple or set. iterate means we can go one by one and check each item in the collection.. 


# for j in "bako sofa":         #"bako sofa" is an iterable
#     print(j)

# for item in (1,2,3,4,5):      #(1,2,3,4,5)is an iterable
#     print(item)    

#Nested loop this is a loop in a loop
for item in [1,2,3,4,5]:
    for x in ["a", "b", "c"]:   #nested loop
        # print(item)
        print(item, x)
    
#how nested look works: python interpreter starts with the loop above 1, now runs all the objects
#in the nested loop, i.e 1,a 1,b 1,c.. before moving to the next item 2,a 2,b 2,c..it runs the 
#only when the nested is looped before moving to the next item in the upper loop

#Iterating a dictionary
user = {"name":"James",
        "age":55,
        "can_swim":False}

for i in user:
    print(i)   #this will give us just the values... to get key & value

for b in user.items():
    print(b)    

#this will print in tupple () but to print it without any curly braces    

for key, value in user.items():
    print(key, value)   

for c in user.values():
    print(c)    

for d in user.keys():
    print(d)    
    
#lets build a counter that count the item on our list
#use loop to sum the total on this list below

my_list = [1,2,3,4,5,6,7,8,9,10]    

counter = 0    # first we create a variable outside the loop that is equal to 0 called counter 
#(could be anything) as we need a variable outside the loop that doesnt change

for item in my_list:
    counter = counter + item

print(counter)  #this has to be outside the loop blook if not it will be looped over   





