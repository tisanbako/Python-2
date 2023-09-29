#Tupples are list that are immutable
#Tupple onlu has two methods.. count and index
my_tupple= (1,2,3,4,5)

#my_tupple[1] = 9   this will thorw an erroe as tupple is immutable
print(my_tupple[1])         #2
print(5 in my_tupple)       #True

#TUPPLE SLICE
new_tupple = my_tupple[1:2]      #(2,) it prints with a comma
print(new_tupple)




#we cannot sort, reverse and append etc tupple 

#Remember we can use tupple as a key in a dict eg
user = {(1,2):[1,2,3],
     "greet":"hello",
     "age":12
     }

print(user[(1,2)])         #[1, 2, 3]


my_tupple = (1,2,3,4,5,6)
x = my_tupple[0]       #1
y = my_tupple[1]       #2
z = my_tupple[2]       #3 

#easie3 way to achieve this is to use unpacking

x,y,z, *other = (1,2,3,4,5,)
print(x)
print(y)
print(z)
print(other)



