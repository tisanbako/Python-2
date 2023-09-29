# # m1 = "Avong"
# # m2 = m1.split("o")
# # print(m2)

# # basket2 = [1,2,0,4,5]
# # new_basket2 = basket2.extend([12])
# # print(new_basket2)


# # [start:stop at:stepover]

# # range_rover = [6,3,8,2,9,4,1,5,7,0]


# # print(range_rover[0:8])

# # age = 2

# # if age >= 12:
# #     print("i am bigger")
# # else:
# #     print("i am smaller")    

# # print(age <= 22)
# # print(age != 2)

# # username = input("what is your usernam: ")
# # password = input ("put in your password: ")

# # password_length = len(password)
# # secret_password = ("*" * password_length)
# # print(f"{username}, your secret {secret_password} length is {password_length}")
# # print(f"{username}, your password {secret_password} is correct, you can log in now")


# # engineer_name = "Benjamin"
# # engineer_name[0] = "v"
# # print(engineer_name)


# # l3 = "stephen"
# # l3 = l3.replace("s", "j")
# # print(l3)

# # names = ["joe", "ben", "nike"]
# # names[0] = "jerry"
# # print(names)


# # m1 = "jjtech"
# # m2 = "jjtech"
# # print(id(m1))
# # print(id(m2)) 

# # m3 = "james"
# # m4 = "tunde"
# # print(id(m3))
# # print(id(m4))



# # name_1 = "Varun"
# # name_2 = "T" + name_1[1:]





# # print(input("what is yout name"))
# # print(len("benjamin"))
# # print(len(input("did you get the food? ")))

# # lr = 5.4
# # lr3 = round(lr)
# # print(lr3)


# # name = "Avong"
# # name.split("o") #if i remove name2 = and print(name)it will give me avong as methods don't iterate
# # print(name)
# # print(name)
# # name3 = name[1]
# # print(name3)

# # my_cart = ["android", "sagem", "iphone", "samsung"]

# # cart3 = []
# # for a in my_cart:
# #     cart2 = a.replace("android", "hey")
# #     print(cart2)
# #     # cart3.append(cart2) #append put everything in a list
# #     # print(cart3)

# # f1 = ["a", "v", "b", "x" "c", "m",]
# # f2 = f1
# # print(id(f1))
# # print(id(f2))

# # f3 = ["b", "z", "b", "x" "c", "m",]
# # f4 = f3[:]
# # print(id(f3))
# # print(id(f4))

# # txt = "For only {price:.2f} dollars!"
# # print(txt.format(price = 49))
# price = 49
# print(f"You can get it for only {price:.2f} dollars!")

names = ["jay", "bay", "sam"]
names2 = []

names2.append(names[1])
print(names2)

z1 = "jeremiah"
z2 = (z1.replace("j", "ge" ))
print(z2)

names = ["bahbell@bell", "lak@daar", "lak@berger"]
names2 = []

for i in names:
    l2 = i.split("@")

    names2.append(l2[1])
    print(names2)
    print(id(names2)) 
    print(id(i))

saying = ["it", "shall", "not", "be", "well"]
print()
