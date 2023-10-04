



# friends = ["abby", "jonathan", "becky", "ryan", "meghan", "taisia"]

# # print(friends[-1::])         #['taisia']
# print(friends[-1::])                                #taisia  
# print(friends[-5:-1])               #print(friends[-1:-7:-1]) 
# print(friends[-1::-2])              #['taisia', 'ryan', 'jonathan']
# print(friends[-1:-4:-1])             #['taisia', 'meghan', 'ryan']
# print(friends[-1:-7:-1])             #['taisia', 'meghan', 'ryan', 'becky', 'jonathan', 'abby']
# print(friends[::-1])              #['taisia', 'meghan', 'ryan', 'becky', 'jonathan', 'abby']
# print(friends[::1])               #['abby', 'jonathan', 'becky', 'ryan', 'meghan', 'taisia']

# property = "abcdefghi"
#            #123456789
# #[start:stop at:stepover]
# print(property[2:9:1])   #cdefghi
# print(property[0:9:1])   #abcdefghi  
# print(property[::1]) #abcdefghi
# print(property[1:9:1]) #bcdefghi
# print(property[1:]) #bcdefghi


#SET WE CAN SLICE SET SAME WAY WE SLICE LIST AND STR
friends = ("abby", "jonathan", "becky", "ryan", "meghan", "taisia")
print(friends[::-1])  #('taisia', 'meghan', 'ryan', 'becky', 'jonathan', 'abby')
print(friends[-1::])   #('taisia',)
print(friends[-3:-6:-2])  #('ryan', 'jonathan')
print(friends[4::-1])  #('meghan', 'ryan', 'becky', 'jonathan', 'abby')
print(friends[5::-1])  #('taisia', 'meghan', 'ryan', 'becky', 'jonathan', 'abby')