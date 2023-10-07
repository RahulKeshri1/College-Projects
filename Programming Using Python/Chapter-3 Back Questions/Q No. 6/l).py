n=5
k=n-1
for i in range(1,n):
    print("  "*k,end="")
    for j in range(2*i-1):
        print("* ",end="")
    print()
    k-=1

k=2
for b in range(n-2,0,-1):
    print("  "*k,end="")
    for j in range(2*b-1):
        print("* ",end="")
    print()
    k+=1
