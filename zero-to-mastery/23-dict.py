#Dictionary are unorder key value pair. dict is not sorted like list. dict has a key:value pair
#we use the key to access/grab the value. dict are alloverthe place in the memory. they are scattered i.e
#you don't get them in order of how you write them.
dictionary = {"a":1, "b":2, "c":"man"}
print(dictionary["a"])          #here we alooking for the value of 'a' which is 1, so we tell key "a' to grab the value
# print(dictionary["c"])    #error as no key "c" is not on the dict

dictionary2 = {
    "a":[1,2,3],
    "b":"hello",
    "x":True
}

print(dictionary2["a"])
print(dictionary2["a"][1])        #to get the index of 1 in the "a key


#lets create a dictionary in a list
my_list = [{"a":[4,5,6], "b":"hello", "x":True}, {"a":[1,2,3], "b":"hello", "x":True}]
print(my_list[0]["a"][2])     #6 the first from the list the first item in the array, 
#the "a" key and the third [2] item in the a key

#DICT KEYS
#dict value can be anything like what we have abouve ..THE KEY OF A DICTIONARY CAN BE THAT IS NOT IMMUTABLE 
#EG float, tupple, bool, str, int

l1 = {123:[123],
      True:"hello"
      #[100]:True   #if we print[100] it will give an error as lists are mutable
      }

#note 99% of the time a key will be something descriptive like a str

#a key has to be unique or else it will be overriden eg

a = {"444":[1,2,3],
     "444":"jerry"}
print(a["444"])         #jerry as the second key444 overrides the first key 444

#key needs to be unique and can only be appear once or else it will be overriden
user = {"basket":[1,2,3],
     "greet":"jerry"}
#print(user["age"])    #this will give us an error, and error stops our program. to avoid this we can use the get method
print(user.get("age"))     #this will give us None 

#But what if we want to assign a value to a key we don't have declared
user1 = {"basket":[1,2,3],
     "greet":"jerry"}
print(user1.get("age", 22))        #it'll print 22

#Note if we have aged declared as a key, it will overide what we have on the print function eg
user2 = {"basket":[1,2,3],
     "greet":"jerry",
     "age":12
     }

print(user2.get("age", 22))        #it'll print 12 as 12 is declared. 22 is incase it is not declared



#you can also dictionary by using the built-in ffunction dict
info = dict(name="john")
print(info)

#note name does not have quotation mark