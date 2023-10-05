#enumerate gets us the index of the object we want to iterate(loop)

for i in enumerate("helloooo"):
    print(i)   #this will loop helloooo with index wrapped in bracket 

#we can remove the bracket by unpacking eg  

for b,char in enumerate("helloooo"):     #b is the index, char is character
    print(b, char)     #check the diff

for c,char in enumerate([1,2,3,4,4]):   #list
    print(c, char)     

for d,char in enumerate((1,2,3,4,4)):   #tupple
    print(d, char)     


for e,char in enumerate(range(10)):   
    print(e, char)    #this prints the range 0-9 and their index

#EXERCISE
# Say we want to see the index of 50 from 0-99

for f,c in enumerate(range(100)):
    #print(f,char)
    if c == 50:
        print(f"index of 50 is {f}")   