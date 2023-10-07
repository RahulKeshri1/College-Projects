#This method can be used to print the Hollow inverted Triangle but it uses 2 loop
"""n=4
j=0
for i in range(n,0,-1):
    print("  "*j,end=" ")
    for k in range(2*i-1):
        if k==0 or k==2*i-2 or i==n:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    j+=1"""

#This method can be used to print the Hollow inverted Triangle but it uses single loop, so it is well optimised.
n=int(input("Enter the number of lines.:\t"))
k=0
m=2*n-4
for i in range(n):
    print("  "*k,end=" ")
    if i==0:
        print("* "*(2*n-1))
    elif i==n-1:
        print("* ")
    else:
        print("* ","  "*m,"* ")
    m-=2
    k+=1