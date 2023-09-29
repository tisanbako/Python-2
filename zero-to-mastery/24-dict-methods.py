user = {"basket":[1,2,3],
     "greet":"hello",
     "age":12
     }

#MY EXPERIMENT
# if "hello" in user.values():
#     print("yes it is in")
# else:
#     print("it's not")    

#we can check if an item ic present in a dict just like in list eg
print("basket" in user)    #True.. does basket exist in user?
print("name" in user)         #False

print("age" in user.keys())    #True
print("jerry" in user.values())       #False
print("hello" in user.values())   #True      
print(user.items())             #dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 12)])... this creats a tupple
# print(user.clear())           #None clears everything 
# user.clear()              #{} creats an empty dict
# print(user)

user2 = user.copy()
print(user2)
#now even if you delete user, you still have all the values of user2 because we copy everything to user2
user.update({"age":35})
print(user)

user.update({"hobby":"reading"})
print(user)


