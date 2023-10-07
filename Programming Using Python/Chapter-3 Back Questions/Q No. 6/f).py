n=5
for i in range(n):
    for j in range(n):
        if (j==1 or j==2 or j==3) and (i==1 or i==2 or i==3):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()