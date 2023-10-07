n=5
j=0
for i in range(1,n+1):
    print("  "*j,end=" ")
    for k in range(i,n+1):
        print("$",end=" ")
    print()
    j+=1