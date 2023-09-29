#_____________________________________________________________________________________________
#Write a Program in Python to do a Menu driven Program in for two Matrices entered by User.
#Menu:-Transpose, Addition, Multiplication, Subtraction, 
#_____________________________________________________________________________________________
import numpy as np

#Function to take input the elements of a Matrix.
def input_matrix(matrix,row,col,k=""):    
    for i in range(row):
        for j in range(col):
            print("Enter the element at ",i+1," th * ",j+1," th position in the",k,"Matrix:",end="\t")
            matrix[i][j]=int(input())
    return matrix

#Function to find the Transpose of a Matrix.ṇ
def transpose(arr,row,col):
    ans=np.zeros((col,row))

    for i in range(col):
        for j in range(row):
            ans[i][j]=arr[j][i]
    
    return ans

#Function to Add two Matrices.
def addition(arr1,row1,col1,arr2,row2,col2):
    if row1!=row2 and col1!=col2:
        print("We can not perform Addition because the Dimensions of both the Matrices are not same.")
        return " "
    else:
        ans=np.zeros((row1,col1))
        for i in range(row1):
            for j in range(col1):
                ans[i][j]=int(arr1[i][j])+int(arr2[i][j])
        return ans

#Function to Subtract two Matrices.
def subtraction(arr1,row1,col1,arr2,row2,col2):
    if row1!=row2 and col1!=col2:
        print("We can not perform Subtraction because the dimensions of both the matrices are not same.")
        return " "
    else:
        n=int(input("If You want to subtract 2nd matrix from the 1st matrix then enter 1 else enter 2:\t"))
        
        if n==1:
            ans=np.zeros((row1,col1))
            for i in range(row1):
                for j in range(col1):
                    ans[i][j]=int(arr1[i][j])-int(arr2[i][j])
        else:
            ans=np.zeros((row1,col1))
            for i in range(row1):
                for j in range(col1):
                    ans[i][j]=int(arr2[i][j])-int(arr1[i][j])
    return ans

#Function to Perform Scalar Multiplication.
def multiplication(arr,row,col,k):
    for i in range (row):
        for j in range(col):
            arr[i][j]*=k
    
    return arr

#Function to Check whether The Matrix is Symmetric or Skew Symmetric.
def check(arr,row,col):
    sym=0
    skw=0
    for i in range(row):
        for j in range(col):
            if (arr[i][j] == - arr[j][i]) or arr[i][i]==0:
                skw+=1
            elif arr[i][j]==arr[j][i]:
                sym+=1
            else:
                break
        if arr[i][j]!=arr[j][i] and arr[i][j] != -arr[j][i]:
            break

    if sym==row*col:
        print("The Matrix is Symmetric Matrix.!")
    elif skw==row*col:
        print("The Matrix is Skew Symmetric Matrix.!")
    else:
        print("The Matrix is neither Symmetric Matrix nor Skew Symmetric Matrix.")
    return ""

#Function to Check Whether Two Matrices are Equal or Not.
def equal(arr1,row1,col1,arr2,row2,col2):
    if row1!=row2 and col1!=col2:
        print("We can not Check the Equality of the two Matrices because the dimensions of both the matrices are not same.")
        return ''
    else:
        counter=0
        for i in range(row1):
            for j in range(col1):
                if arr1[i][j]==arr2[i][j]:
                    counter+=1
                else:
                    break
            if arr1[i][j]!=arr2[i][j]:
                break

        if counter==row1*col1:
            print("Both The Matrices are Equal.")
        else:
            print("Sorry!! Both The Matrices are not Equal.")
    return ""

#Function to Multiply Two Matrices.
def multiply(arr1,row1,col1,arr2,row2,col2):
    if row1!=col2:
        print("The two Matrices are not Multiplicable.")
        return ""
    else:
        ans=np.zeros((row1,col2))
        for i in range(row1):
            for j in range(col2):
                sum=0
                for k in range(row2):
                    sum+=int(arr1[i][k])*int(arr2[k][j])
                ans[i][j]=sum
    print("Matrix after performing Matrix Multiplication:\t")
    return ans

#Main Function.
def main():
    row1=int(input("Enter the No. of Rows in 1st Matrix:\t"))
    col1=int(input("Enter the No. of Columns in 1st Matrix:\t"))
    arr1=np.zeros((row1,col1))
    
    #Taking input The elements of First Matrix.
    arr1=input_matrix(arr1,row1,col1,1)
    
    #Asking user to whether s(he) wants to enter 2nd Matrix or not.
    print("Do you want to input 2nd Matrix? (y/n)\t")
    c=input()
    if c in ("y","Y","yes","Yes","YES"):
        row2=int(input("Enter the No. of Rows in 2nd Matrix:\t"))
        col2=int(input("Enter the No. of Columns in 2nd Matrix:\t"))
        arr2=np.zeros((row2,col2))

        #Taking Second Matrix Element Input.
        arr2=input_matrix(arr2,row2,col2,2)

    ch='y'                                                     #To iterate into the Loop.
    menus="\n Menus:\n 1.Transpose.\n 2.Addition of two Matrices.\n 3.Subtraction of two Matrices.\n 4.Scalar Multiplication of a Matrix.\n 5.Checking if the input Matrix is Symmetric or Skew-Symmetric Matrix.\n 6.Checking if two Matrices are equal or not.\n 7.Matrix Multiplication."
    print(menus)
    print("Enter the operation you want to perform:\t")

    
    while ch in ("y","Y","yes","Yes","YES"):
        op=input()                                             #Choice to take the operation to perform


        if op in ("1","Transpose","transpose","transp","TRANSPOSE","transpose"):
            if c in ("y","Y","yes","Yes","YES"):
                print("Which Matrix's Transpose You want to find?\t 1 or 2?\t")
                choice=input()                                 #Choice to Find the Transpose of which Matrix?
                if choice=="1":
                    arrans=transpose(arr1,row1,col1)
                    print(arrans)
                else:
                    arrans=transpose(arr2,row2,col2)
                    print(arrans)
            else:
                arrans=transpose(arr1,row1,col1)
                print(arrans)

        elif op in ("2","Addition","addition","add","Add"):
            if c in ("y","Y","yes","Yes","YES"):
                if row1==row2 and col1==col2:
                    arrans=addition(arr1,row1,col1,arr2,row2,col2)
                    print(arrans)
                else:
                    print("Sorry!!\nThe dimensions of both the Matrices are not equal so we can't Perform Addition on it.")
            else:
                print("You have not Entered the Second Matrix")
        
        elif op in ("3","Subtraction","subtraction","sub","Sub"):
            if c in ("y","Y","yes","Yes","YES"):
                if row1==row2 and col1==col2:
                    arrans=subtraction(arr1,row1,col1,arr2,row2,col2)
                    print(arrans)
                else:
                    print("Sorry!!\nThe dimensions of both the Matrices are not equal so we can't Perform Subtraction on it.")
            else:
                print("You have not Entered the Second Matrix")

        elif op in ("4","Scalar Multiplication","scalar multiplication","multiplication"):
            if c in ("y","Y","yes","Yes","YES"):
                print("In which Matrix you want to perform Scalar Multiplication?\t 1 or 2?\t")
                choice=input()                                 #Choice to Find the Matrix in which Scalar Multiplication has to be performed?
                k=int(input("Enter the Number You want to multiply to the Matrix:\t"))
                if choice=="1":
                    arrans=multiplication(arr1,row1,col1,k)
                    print(arrans)
                else:
                    arrans=multiplication(arr2,row2,col2,k)
                    print(arrans)
            else:
                arrans=multiplication(arr1,row1,col1,k)
                print(arrans)

        elif op in ("5","Check","check"):
            if c in ("y","Y","yes","Yes","YES"):
                print("In which Matrix you want Check?\t 1 or 2?\t")
                choice=input()                                 #Choice to Find the Matrix in which Checking has to be performed?
                if choice=="1":
                    arrans=check(arr1,row1,col1)
                    print(arrans)
                else:
                    arrans=check(arr2,row2,col2)
                    print(arrans)
            else:
                arrans=check(arr1,row1,col1)
                print(arrans)
        
        elif op in ("6","Equality","equality","Check Equal","check equal","equal"):
            if c in ("y","Y","yes","Yes","YES"):
                if row1==row2 and col1==col2:
                    arrans=equal(arr1,row1,col1,arr2,row2,col2)
                    print(arrans)
                else:
                    print("Sorry!!\nThe dimensions of both the Matrices are not equal so we can't Perform Addition on it.")
            else:
                print("You have not Entered the Second Matrix.")
        
        elif op in ("7","Matrix Multiplication","matrix multiplication","matrix","Matrix"):
            if c in ("y","Y","yes","Yes","YES"):
                arrans=multiply(arr1,row1,col1,arr2,row2,col2)
                print(arrans)
            else:
                print("You have not Entered the Second Matrix.")       
        
        else:
            print("Invalid Choice Please Choose from the Menu\t",menus)
            continue
        
        print("Do you want to perform any other action(s)?\t")        
        ch=input()
        if ch in ("n","N","no","No","NO","not","Not","NOT"):    #Choice to Continue to the Program.
            print("Thank You for your Valuable time.")
            break
        print("Do you want to see the Menu?\t")
        menu=input()                                            #Choice To display the Menu.
        if menu in ("y","Y","yes","Yes","YES"):
            print(menus)
        else:
            print("Enter the operation you want to perform:\t")


main()