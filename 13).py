#____________________________________________________________________________________________
#   write a Program to accept a name from a user. Raise and handle appropriate exception(s)
#   if the text entered by the user contains digits and/or special characters.
#____________________________________________________________________________________________

name=input("Enter the name:\t")
flag=0
try:
    for i in range(len(name)):
        if name[i].isdigit():
            raise ValueError("name cannot contain digit")
        elif name[i].isalpha():
            flag+=1
        else:
            raise ValueError("Name cannot contain special character")
except ValueError as err:
    print("Error:\t",err)