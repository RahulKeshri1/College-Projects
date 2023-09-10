#_____________________________________________________________________________________
# Write a Program in Python to Multiply two Matrices.
#_____________________________________________________________________________________

row1=int(input("Enter the number of rows in first matrix:\t"))
col1=int(input("Enter the number of columns in first matrix:\t"))

list1=[[0]*col1 for i in range(row1)]

import numpy as np

for i in range (0,row1):
    for j in range(0,col1):
        print("Enter the elements in ",i+1,"th * ",j+1,"th position in the first matrix:",end="\t")
        list1[i][j]=input()

row2=int(input("Enter the number of rows in second matrix:\t"))
col2=int(input("Enter the number of columns in second matrix:\t"))

list2=[[0]*col2 for i in range(row2)]

for i in range (0,row2):
    for j in range(0,col2):
        print("Enter the elements in ",i+1,"th * ",j+1,"th position in the second matrix:",end="\t")
        list2[i][j]=input()

listans=[[0]*col2 for i in range(row1)]
sum=0

l1=np.array(list1)
l2=np.array(list2)

if(col1!=row2):
    print("We can't multiply two matrices if number of rows in first matrix is not equal to number of columns in second matrix\t")

elif(col1==row2):
    for i in range(row1):
        for j in range(col2):
            for k in range(row2):
                sum+=int(l1[i][k])*int(l2[k][j])
            listans[i][j]=sum
            sum=0

listans=np.array(listans)   
print("The Matrix after performing the Matrix Multiplication:\t")   
print(listans)