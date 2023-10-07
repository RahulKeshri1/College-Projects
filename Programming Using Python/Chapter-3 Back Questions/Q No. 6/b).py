n=5
for i in range(1,n):
    for j in range(4-i,0,-1):
        print(end="  ")
    for k in range(i,0,-1):
        print(k,end=" ")
    for l in range(2,i+1):
        print(l,end=" ")
    print()