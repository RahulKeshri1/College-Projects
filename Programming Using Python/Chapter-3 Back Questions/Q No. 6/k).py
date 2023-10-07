n=4
k=n-1
for i in range(1,n+1):
    print("  "*k,end="")
    for l in range(1,2*i):
        if l==1 or l==2*i-1 :
            print("* ",end="")
        else:
            print("  ",end="")
    k-=1
    print()
k=1
for i in range(n-1,0,-1):
    print("  "*k,end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print("* ",end="")
        else:
            print("  ",end="")
    k+=1
    print()