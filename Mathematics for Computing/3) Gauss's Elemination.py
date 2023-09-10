#_____________________________________________________________________________________________________________________
#Write a Program in Python to take input from the user in a matrix and convert it into Upper Triangular Matrix.
#_____________________________________________________________________________________________________________________

#   Function to convert a Matrix into Echolen Form using Gauss's Elemination Method.
#   row=Number of rows in the Matrix,  
#   col=Number of Columns in the Matrix,    
#   a=Matrix in which we have to perform the operation.
def Gauss_Elemination(row,col,a):       
    for j in range(row):
        pv=j
        for i in range(j+1,row):
            q1=a[pv][j]/a[i][j]
            for k in range(col):
                a[i][k]=round((a[pv][k]-q1*a[i][k]),2)
    
    return a

#Function to take Matrix element input.
#   row=Number of rows in the Matrix,  
#   col=Number of Columns in the Matrix,    
#   a=Matrix in which we have to perform the operation.
def input_matrix(row,col,a):
    #Matrix Input.
    for i in range(row):
        for j in range(col):
            print("Enter the number at ",i+1,"th * ",j+1,"th position",end="\t")
            a[i][j]=int(input())
    return a

#Main Function
def main():
    import numpy as np

    row=int(input("Enter the Number of Rows in Matrix:\t"))
    col=int(input("Enter the Number of Columns in Matrix:\t"))

    #Defining a Matrix of order row*col
    matrix=np.zeros((row,col))
    ans=np.zeros((row,col))


    if row==col-1:
        matrix=input_matrix(row,col,matrix)
        print("\n The Entered Matrix is Determined!!")
        ans=Gauss_Elemination(row,col,matrix)
        print(ans)

    elif row>col-1:
        matrix=input_matrix(row,col,matrix)
        print("\n The Entered Matrix is Over Determined!!")
        ans=Gauss_Elemination(row,col,matrix)
        print(ans)

    else:
        print("\n The Entered Matrix is Under Determined!!")

if __name__=="__main__":
    main()

    input()