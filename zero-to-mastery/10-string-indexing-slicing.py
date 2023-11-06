selfish = "me me me".
         # 01234567
print(selfish[0]) #m
print(selfish[1]) #2
print(selfish[2]) # space


#SLICING - this is used to access different part of a string and list
property = "abcdefghi"
           #123456789
#[start:stop at:stepover]
print(property[2:9:1])   #cdefghi
print(property[0:9:1])   #abcdefghi  
print(property[::1]) #abcdefghi
print(property[1:9:1]) #bcdefghi
print(property[1:]) #bcdefghi
print(property[:3])    #  abc    
print(property[1:8:2]) #bdfh
print(property[-1]) #1 printing on reverse mode
print(property[::-1]) #ihgfedcba
print(property[::-2]) #igeca

name_1 = "Varun"
name_2 = "T" + name_1[1:]
print(name_2)         #Tarun
