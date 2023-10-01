my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))             #{1, 2, 3} show the difference
print(your_set.difference(my_set))            #{6, 7, 8, 9, 10}
# my_set.discard(5)            #{1, 2, 3, 4} CHECK DIFF BWN DISCARD AND REMOVE
# print(my_set)

# my_set.difference_update(your_set)   #{1, 2, 3}Remove all elements of yourset another set from myset.
# print(my_set)

print(my_set.intersection(your_set))   #{4, 5} Return the intersection of two sets as a new set. 
#i.e. all elements that are in both sets. i.e elemets they have in common
print(my_set & your_set)  #same with intersection

print(my_set.union(your_set))  #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} join both sets.. it does it without duplicates
print(my_set | your_set)  #same with union

print(my_set.isdisjoint(your_set))    #False ..Return True if two sets have a null intersection. i.e if they have don't have anything in common


a_set = {4,5}
b_set = {4,5,6,7,8,9,10}

print(a_set.issubset(b_set))       #True is a_set a subset of b_set  

print(a_set.issuperset(b_set))     #False b_set a a subset of a_set? i.e does everything in b.set in a.set?
print(b_set.issuperset(a_set))     #True b_set contain everythinf in a_set