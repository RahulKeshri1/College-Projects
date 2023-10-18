#____________________________________________________________________________________________
#   write a Program to accept a name from a user. Raise and handle appropriate exception(s)
#   if the text entered by the user contains digits and/or special characters.
#____________________________________________________________________________________________

def check(name):
    counter=0
    for i in range(len(name)):
        if name[i]>='0' and name[i]<='9':
            return "A Name can not contain any number."
        elif (name[i]>='a' and name[i]<='z') or (name[i]>='A' and name[i]<='Z') or name[i]==" ":
            counter+=1
        else:
            return "A Name can not contain any Special Character."
    if counter==len(name):
        return "Entered Name is Perfect."
def main():
    name=input("Enter you name:-\t")
    ans=check(name)
    print(ans)

main()