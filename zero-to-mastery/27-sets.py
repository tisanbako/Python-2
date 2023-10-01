# #sets are unorder set of unique object. no duplicate eg sets are unordered
my_set = {2,1,2,3,4,2,5}
print(my_set)                 #{1, 2, 3, 4, 5} it removes the duplicates of 2

my_set2 = {1,2,3,4,5,5,8}
my_set2.add(100)        #{1, 2, 3, 4, 5, 100, 8} it adds the 100      
my_set2.add(4)      
print(my_set2)            #{1, 2, 3, 4, 5, 100, 8} it doesnt add the 4 cuz it exist already.. no duplicate

#Converting a list to a set
my_list3 = my_set2 = [4,2,3,1,5,5,8]
print(set(my_list3))              #{1, 2, 3, 4, 5, 8}
#you use this when you have usernames or emails when you don't want duplicates, so you dont keepsending to sam email over and over


#set objects does not support indexing ed
my_set4 = {1,4,2,3,4,5,5,8}
# print(my_set4[1])   #it will throw an error 'set' object is not subscriptable 

#the way to check if comething exist in a set is to use the "in" eg
print(1 in my_set4)     #True

print(len(my_set4))      #6, it does not count duplicates

#we can convert the set to a list eg
print(list(my_set4))   #[1, 2, 3, 4, 5, 8] it does it while removing the duplicates

my_set4 = {1,4,2,3,4,5,5,8}
new_sett = my_set4.copy()   #{1, 2, 3, 4, 5, 8} copies without duplicating
print(new_sett)

my_set4.clear()
print(my_set4)     #set() empty set

