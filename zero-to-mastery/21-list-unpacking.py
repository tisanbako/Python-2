# #we can change a list in different ways ealier we did something like
# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# #or even when we put the values in a list
# a,b,c = [1,2,3]
# print(a)
# print(b)
# print(c)

#Unpacking
#a,b,c = [1,2,3,4,5,6,7,8,9]

#what if we want to 1,2,3 but keep everything else in a list? we just comma
#the c, and add *other eg
a,b,c, *other = [1,2,3,4,5,6,7,8,9] #[4, 5, 6, 7, 8, 9]
print(other) 

#what if we add d 
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9] 
print(other)   #[4, 5, 6, 7, 8]
print(d)     #9 the very last item

a,b,c, *other, d, e = [1,2,3,4,5,6,7,8,9] 
print(other)   #[4, 5, 6, 7, 8]
print(d)     #8
print(e)     #9