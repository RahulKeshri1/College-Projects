#_____________________________________________________________________________________
# Write a Program in Python to Multiply two Matrices.
#_____________________________________________________________________________________

row1=int(input("Enter the number of rows in first matrix:\t"))
col1=int(input("Enter the number of columns in first matrix:\t"))

import numpy as np

list1=np.zeros((row1,col1))

for i in range (0,row1):
    for j in range(0,col1):
        print("Enter the elements in ",i+1,"th * ",j+1,"th position in the first matrix:",end="\t")
        list1[i][j]=input()

row2=int(input("Enter the number of rows in second matrix:\t"))
col2=int(input("Enter the number of columns in second matrix:\t"))

list2=np.zeros((row2,col2))

for i in range (0,row2):
    for j in range(0,col2):
        print("Enter the elements in ",i+1,"th * ",j+1,"th position in the second matrix:",end="\t")
        list2[i][j]=input()

l1=np.array(list1)
l2=np.array(list2)

if(col1!=row2):
    print("We can't multiply two matrices if number of rows in first matrix is not equal to number of columns in second matrix\t")

elif(col1==row2):
    listans=np.matmul(l1,l2)

print(listans)