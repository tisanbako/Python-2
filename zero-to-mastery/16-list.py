#list is an order sequence of object that can be of anytype.
#denotes with square bracker. list is a collection of items. eg

li = [1,2,3,4,5,6]
li2 = ["a", "b", "c", "d"]
li3 = [1,2, "a", 2.5, "joe", True] #

#DATA STRUCTURE

amazon_cart = ["notebooks", "sunglasses"]
print(amazon_cart[0])
print(amazon_cart[1])


#list slicing. 

walmart_cart = ["notebooks", "sunglasses", "toys", "grapes"]
print(walmart_cart)
print(walmart_cart[0:2])
print(walmart_cart[0::2]) #skip every second one

#list are mutable (we can change them) unlike str which are not
walmart_cart[0] = "laptop" #replacing notebook with Bible
print(walmart_cart)         #['laptop', 'sunglasses', 'toys', 'grapes']
print(walmart_cart[1:4])     #start from, index of 1 (sunglasses and stop at index of 4 (grapes))
print(walmart_cart[0:3])     #['laptop', 'sunglasses', 'toys']               
                
 #everytime we do slicing we creat a new copy og the list eg.

alibaba = ["short", "runner", "glasses", "phone", "shoes"]
alibaba2 = alibaba[0:3] #we're giving alibaba2 the valie of alibaba from index 0-3
alibaba2[0] = "trouser"
print(alibaba2)           #['trouser', 'runner', 'glasses']
print(alibaba)        #['short', 'runner', 'glasses', 'phone', 'shoes']

#what happenes if we change the second variable to the values of the first variable eg
cart1 = ["macbook", "books", "bucker", "yam"]
cart2 = cart1
cart2[0] = "window"
print(cart2)     #['window', 'books', 'bucker', 'yam']
print(cart1)     #['window', 'books', 'bucker', 'yam']

#they both have thesame output because the cart1 is in the memory, 
# so when we say cart2 is equal to what we have of memory of cart1.
# so if we alter cart2 it'll alter cart1 as they both share same value in the momory.

#there's a difference with modifying a list and copying a list. 
#to maintain different values  we have to include [:] to the new variable eg
my_cart = ["android", "sagem", "iphone", "samsung"]
my_cart2 = my_cart[:]
my_cart2[0] = "nokia"
print(my_cart2)
print(my_cart)

#there's a difference with modifying a list and copying a list. 

#lets create a dictionary in a list
my_list = [{"a":[4,5,6], "b":"hello", "x":True}, {"a":[1,2,3], "b":"hello", "x":True}]
print(my_list[0]["a"][2])     #the first from the list the first item in the array, 
#the "a" key and the third [2] item in the a key


#Rememember, list are mutable eg
name = [2,3,4]
name[0]=5
print(name)

#but float, tupple, int, str are not mutable eg
# name2 = "Jeremiah"
# name2[0]= "g"
# print(name2)        it will throw an arror and str objects dont support reassignment