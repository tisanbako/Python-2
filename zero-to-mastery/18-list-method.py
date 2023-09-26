#
basket = [1,2,3,4,5]

#adding
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


#insert .. this is adding something in a specific place e.g
basket2 = [1,2,0,4,5]
new_basket2 = basket2.insert(3, 100)   #this will return none. as methods modify the list in place
#it doesn't output a new list. it just modify what is already in the list
basket2.insert(3, 100) #insert 100 at the index of 3
print(basket2)

basket3 = [1,2,0,4,5]
basket.extend(13)
print(basket3)
