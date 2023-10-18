#________________________________________________________________________________________________
#   Consider a tuple t1=(1,2,5,7,9,2,4,6,8,10). Write a Program to perform following operations:
#       a) Print half the values of the tuple in one line and the other half in the next line.
#       b) Print another tuple whose valus are even numbers in the given tuple.
#       c) Concatenate a tuple t2=(11,13,15) with t1
#       d) Return maximum and minimum value from this tuple.
#________________________________________________________________________________________________

def a(tuple):
    le=len(tuple)
    x=le//2
    for i in range(x):
        print(tuple[i],end=" ")
    
    print()
    
    for j in range(x,le):
        print(tuple[j],end=" ")
    print()

def b(tup):
    l1=[]
    for i in range(len(tup)):
        if tup[i]%2==0:
            l1=l1+[tup[i]]
    t1=tuple(l1)
    return t1

def main():
    t=(1,2,5,7,9,2,4,6,8,10)
    a(t)
    next=b(t)
    print("The tuple consisting of even numbers:\t",next)

    t2=(11,13,15)
    t+=t2
    print("The tuple after concationation=",t)
    print(f"The maximum value of this tuple={max(t)}\n The minimum value of this tuple={min(t)}")

    

main()
