#_____________________________________________________________________________________

#  Write a Program in Python to Find the Transpose of a Matrix.
#_____________________________________________________________________________________

import numpy as np
row=int(input("Enter the number of rows in the matrix:\t"))
col=int(input("Enter the number of columns in the matrix:\t"))
arr=np.zeros((row,col))


for i in range(row):
    for j in range(col):
        print("Enter the element at ",i+1," th * ",j+1," th position in the Matrix:",end="\t")
        arr[i][j]=input()

ans=np.zeros((col,row))
for i in range(col):
    for j in range(row):
        ans[i][j]=arr[j][i]

print("Matrix before Transposing.")    
print(arr)
print("Matrix after Transposing.")
print(ans)
