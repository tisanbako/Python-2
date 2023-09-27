#
basket = [1,2,3,4,5]

#ADDING
new_basket = basket.append(100)
print(basket)    #[1, 2, 3, 4, 5, 100]
print(new_basket)   #None  .. this is because methods (.append(in this case)) 
#or any other method does not produce a value, all it does it change the already existing value 
#already existing value i.e basket. best way to get a new value for 
# new_basket is lets say we want to add 200
basket.append(200)
new_basket = basket
print(basket)
print(new_basket)
#after we append to basket, we can now assign basket to new basket

#an example of what we did on list.py with cart1 and cart2
new_basket.append(300)
print(basket)
print(new_basket)



basket2 = [1,2,0,4,5]
new_basket2 = basket2.insert(3, 100)  #insert .. this is adding something in a specific place e.g
 #this will return none. as methods modify the list in place
#it doesn't output a new list. it just modify what is already in the list
basket2.insert(3, 100) #insert 100 at the index of 3
print(basket2)


basket3 = [6,2,0,4,5]
basket3.extend([13])
# basket3.extend([13]) #if i wrapped this up with a print eg print(basket3.extend([13])) 
#it will return zero as methoths need to be tied to an object in this case a 
# variable basket4 = basket3.extend([13])
#Also extend [] because extend 
print(basket3)

#Removing
basket4 = [6,2,8,0,4,5]
basket4.pop()   #5 gets removed.. pop removes to the right
print(basket4)
basket4.pop()   #4 gets removed
print(basket4)

basket5 = [1,2,3,0,4,8] 
basket5.pop(2) #removed the index of 2 (3)
print(basket5)

basket5.remove(8)  #removes 8
print(basket5)

#note with remove we give the number we want to remove and pop, we give 
#the index we want to remove

basket6 = [1,2,3,0,4,8] 
basket6.clear()   #clears eveything in the list
print(basket6)

basket7 = ["a", "b", "c", "d", "e", "b"]
print(basket7.index("c"))  #finding the index of "c"

print("d" in basket7) #(True)to check if d is in basket 7  True

print("j" in "jeremiah")

print(basket7.count("b"))  #count many time "b" comes up in the list

basket7.sort()  #['a', 'b', 'b', 'c', 'd', 'e'] to rearrange (sort) the list
print(basket7)

basket8 = ["a", "b", "c", "d", "e", "b"]
basket8.reverse()
print(basket8)

#what if we want to reverse it in a sorted way
basket9 = ["c", "b", "f", "d", "e", "a"]
basket9.sort()
basket9.reverse()
print(basket9)
print(len(basket9))

#we can reverser it back by using the reverse method or slicing eg
print(basket9[::-1])  #-1 to print from the right or last object