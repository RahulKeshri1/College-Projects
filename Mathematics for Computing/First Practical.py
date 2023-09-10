#_____________________________________________________________________________________

#  Write a Program in Python to calculate the fair price when travelling from
#  one point to another in a fully connected road network.
#_____________________________________________________________________________________

#Rows and Columns initialisation.
dest=int(input("Enter the number of destinations:\t"))

#List initialisation.
list=[[0]*dest for i in range (dest)]

#Fare Prices/Weights Entry.
print("Enter the fare prices:\t")
for i in range(0,dest):
    for j in range(i,dest):
        if (i!=j):
            print("Enter the price for moving from point ",i+1," to ",j+1,end=":\t")
            list[i][j]=int(input())
            list[j][i]=list[i][j]
            print()

print("Enter the starting point(1,",dest,"):\t")
i=int(input())          #i=row indexing
print("Enter the starting point (1,",dest,"):\t")
j=int(input())          #j=column indexing

if (i>dest or j>dest) :
    print("Invalid Input, You can try entering values between 1 to ",dest," as there are only ",dest," destination(s).")
else:
    print("Fare price for moving from",i," to ",j," is ",list[i-1][j-1])