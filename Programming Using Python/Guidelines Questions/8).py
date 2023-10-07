#_________________________________________________________________________________________________________
#   Write a Program to create a list of the cubes of only the even integers appearing in the input list
#   (may have elements of other types also) using the following:
#       a) 'for' loop
#       b) list comprehension
#_________________________________________________________________________________________________________

def lis(list_):
    l1=[]
    for i in range(len(list_)):
        if list_[i]>='0' and list_[i]<='9':
            num=int(list_[i])
            if num%2==0:
                l1=l1+[num**3]
    return l1

def main():
    s=input("Enter the string.:-\t")
    ans=lis(s)
    print(f"List consisting the cubes of even digits in the entered string is:-\t{ans}")

main()