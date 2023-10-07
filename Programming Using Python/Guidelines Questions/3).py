#_____________________________________________________________________________________
#   Write a program to create a Pyramid of character "*" and a reverse pyramid.
#_____________________________________________________________________________________

#Function to Print Upper Pyramid of total "l" lines. 
def up(l):
    for i in range(l+1):
        for j in range(l+1-i,1,-1):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print()

#Function to Print Inverted Pyramid of total "l" lines.
def ip(l):
    for i in range(l+1):
        for j in range(i):
            print(" ",end="")
        for k in range(2*(l-i)-1):
            print("*",end="")
        print()

def main():
    n=int(input("Enter the Number of lines you want  to form the Pyramid.:\t"))
    ch=input("Do you want to form the Upper Pyramid?:\t")
    if ch in ("yes","YES","Yes","y","Y"):
        up(n)
    ch=input("Do you want to form the Inverted Pyramid?:\t")
    if ch in ("yes","YES","Yes","y","Y"):
        ip(n)

main()