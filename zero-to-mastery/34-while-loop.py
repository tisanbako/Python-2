#apart fron for loop, there's also a while loop. for while loop, we say 
#while a condition is true, do something.
#the catch in for whilel loop, when something is true,  it keep 
#looping and never stops till we break it. unlike for loop that stops eg

# i = 0

# while i < 50:
#     print(i)  

#if we run this it keep running  000000 till the computer dies
#     #because 0 will always be less that 50. This is what is called an infinite loop.
#     # to avoide that we will have to use a break expression like what have below


i = 0

while i < 50:
    print(i)
    break
    

#what if i want it to be looped 20 times? we need to increase the variable 
#so we don't get an infinite loop

b = 0

while b < 20:
    print(b)
    b += 1   #using augumented assignment



c = 0
while c < 50:
    print(c)
    break    

print("job is done")