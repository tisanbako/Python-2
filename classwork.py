is_magician = True
is_expert = False 

#1. Check if magician AND expert: print "you are a master magician"
#2. check if magician but nit expert: print "atleast you're getting there"
#3. if you're not a magician: "you need magic power"

if is_magician and is_expert:
    print("you are a master magician")

elif is_magician and not is_expert:    
    print("atleast you're getting there")

elif not is_magician:
    print("you need magic power")  


#work on yourself and see suggest what it will print before it prints    
#change the values above True and False  

print(True == 1)    #True python convert 1 to Truthy
print("" == 1)      #False cuz "" is not 1 "" is not a datat type
print([] == 1)
print(10 == 10.0)    
print([] == [])

#== and is are two diiferent things.. == looks at the equality while is looks at the excat thing

print(True is 1)   #False cuz True is not same as 1
print(True is True)     #True cuz true is true stores in same location in memory
print("1" is "1")    #True 
print([] is [])       #False cuz this are two lists and not on same locations in memory
print(10 is 10.0)    #False 10 is not 10.1
a = [1,2,3]
b = [1,2,3]
print(a is b)          #False a and b are two different lists
print(id(a))         #they both have different id
print(id(b))