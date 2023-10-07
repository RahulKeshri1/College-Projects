n=5
k=n-1
for i in range(1,n+1):
    print("  "*k,end=" ")
    for l in range(i):
        print("# ",end="")
    k-=1
    print()