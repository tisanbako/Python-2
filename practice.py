
# # # for a in fruits2:
# # #     print(a)     #this is to iterate the whole list.
# # #     if a == "grapes": 
# # #         print("found the fruit we have been looking for") 
# # #         break


# # # def bako(jeremiah):
# # #     print(f"my name is {jeremiah}")

# # # bako("michael") 
# # # bako("tisan")   
# # # a = 1.75 * 1.75
# # # b = 75 / a
# # # print(b)

# # def calculating_bmi(height, weight):
# #     bmi = weight / height ** 2
# #     print(bmi)
# # calculating_bmi(1.75, 75)    

def student_info(name, age, location):
    return f"Hello {name}, with age {age}, your location is {location}"

all_info = student_info("Tisan", 25, "Lagos")
print(all_info)














# def bako_function():
#     print("hello from bako function")


# bako_function()


# def my_function(mark, number):
#     return mark * number 


# print(my_function(2, 3)  )  

# def greet(name):
#     print("hello", name)
#     print("how do you do", name)

# greet("thomas")    
# greet("Ayo")   


# name = {"na":"james@gmail.com", "girl":"kellis@daar.edu", "man":"mark@yahoo.com"}
# tisan = ["hello", "daniel"]

# for i in name:
#     print(i)

# # name.append(tisan)
# # print(name)

# for i in name:
#     r = i.split("@")
#     # print(r)
#     r2 = r[1]
#     # print(r2)
#     r3 = r2.split(".")
#     tisan.append(r3[0])
#     print(tisan)
#     if tisan == "gmail" or r3[0] == "daar" :
#         print("ok gmail", i)
#     # elif tisan == "daar":
#     #     print("ok daar")
#     else:
#         print("ok yahoo", i)        




# for i in name:

   
   
    # if tisan == "kellis@daar.edu":
    #     print("hello jay", i)
    # elif tisan == "james@gmail.com":
    #     print("jamies whats up", i)
    # else:
    #     print("ok! ok!", i)        
      

    # print(name)
    # print(tisan)
    # print(name)
    # first_split = i.split("@")
    # print(first_split)
    # second_split = first_split[1]
    # print(second_split)
    # third_split = second_split.split(".")
    # print(third_split)
    # tisan.append(third_split[0])
    
    
   
def bako_function(name, surname):
    print("my names are ", name, surname)
    return

bako_function("Jeremiah", "Bako")
bako_function("samuel", "Johnson")       


# def calculate_bmi(height, weight):
#     bmi = (weight/(height * height)) * 10000
#     return bmi

# # height = 162
# # weight = 50

# bmi = calculate_bmi(162, 50)
# print(bmi)


# def my_name(name1):
#     print("hello", name1)
#     return
#     print("this won't print", jerry) #this will not print because the return function is a breaker

# my_name("jerry")  


# def bmi_calculation(weight, height):
#     bmi = (weight/height**2)
#     return bmi

# light = bmi_calculation(75, 1.75)

def total_marks(mark):
    #total = sum(mark)
    #number_of_marks = len(mark)
    average = sum(mark)/len(mark)
    # average_mark_cal = total / average_sunj
    return average

marks = [55,64,75,80,65]
average_mark = total_marks(marks)
print(average_mark)






numbers = [18,62,75,83,45]

print(67.8 * 5)
print(sum(numbers))
print(sum(numbers)/5)



   
