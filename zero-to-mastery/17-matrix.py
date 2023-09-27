#Matrix is a way to describe a multi dimentional list.
#matrix is an array with another array inside of it 
#This is mainly used for pictures and machine learning
matrix = [[1,2,3], [4,5,6], [7,8,9]]
#Here we have main array and sub arrays. we can also have sub array inside the sub array eg
d3 = [[1,2,3], [[0,4,7],4,5,6], [7,[4,5,4],8,6]]


#accessing a multidimentional list eg
mt3 = [[1,2,3], [4,5,6], [7,8,9]]  
print(mt3[0][1])   #2  access the first time [1,2,3] which is the first array and 1 index in the first array
print(mt3[2][2])              #9
print(mt3[0][0])              #1
print(mt3[1][2])               #6




#EXERCISE

A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column = [];        # empty list
for row in A:
  column.append(row[2])
  
print("3rd column =", column)

