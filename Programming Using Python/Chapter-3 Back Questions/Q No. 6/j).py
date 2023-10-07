n=4
k=0
for i in range(n,0,-1):
    print("  "*k,end="")
    for j in range(2*i-1):
        print("*",end=" ")
    k+=1
    print()
    