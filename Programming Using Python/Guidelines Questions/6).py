#_____________________________________________________________________________________
#   Write a Program to swap the first n characters of two strings.
#_____________________________________________________________________________________

def rep(string1,string2,n):
    st1=st2=""
    for i in range(n):
        st2=st2+string1[i]
        st1=st1+string2[i]
    for i in range(n,len(string1)):
        st1=st1+string1[i]
    for i in range(n,len(string2)):
        st2=st2+string2[i]
    print(f"\n Previously String 1 was:- \t {string1}  \n and String 2 was:- \t\t{string2}")
    print(f"\n After swaping String1 has become:- \t'{st1}' \n and String 2 has become:- \t\t'{st2}' ")

def main():
    string1=input("Enter the First String:\t\t")
    string2=input("Enter the Second String:\t")
    n=int(input("\n Enter the Number of letters you want to swap.:\t"))
    rep(string1,string2,n)
    input()

main()