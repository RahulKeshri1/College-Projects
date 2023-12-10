#_____________________________________________________________________________________
#   Write a Program to Accept a Number 'n' and 
#       a. Check if 'n' is prime or not.
#       b. Generate all prime numbers till 'n'.
#       c. Generate first 'n' prime numbers.
#_____________________________________________________________________________________

#Function to check a number for Prime.
def checkprime(num):
    if num<2:
        return " "
    elif num==2:
        return num
    else:
        for i in range(2,(num//2)+1):
            if num%i==0:
                return " "
    
    return num

#Function to Generate all Prime Numbers till "n".
def gpn(num):                       #gpn=Generate Prime till 'n'.
    print("1",end="")
    for i in range(2,num+1):
        ans=checkprime(i)
        if ans!=" ":
            print(",",i,end="")
    print()

#Function to Generate First 'n' Prime Numbers.
def gfnp(num):                      #gfnp=Generate First 'n' Prime numbers .
    counter=0
    i=2
    if num>=1:
        print("1",end="")
    while counter < num-1:
        ans=checkprime(i)
        if ans !=" " :
            print(",",i,end="")
            counter+=1
        i+=1
        
     
    
def main():
    n=int(input("Enter the number:\t"))
    print("Do you want to check this number for prime?\t",end="")
    ch=input()
    if ch in ("yes","YES","Yes","y","Y"):
        ans=checkprime(n)
        if ans!=" ":
            print(n,"is a Prime Number.")
        else:
            print(n," is a not Prime Number.")
    
    print(f"Do you want to Generate all Prime Numbers till {n}?\t",end="")
    ch=input()
    if ch in ("yes","YES","Yes","y","Y"):
        gpn(n)
    
    print(f"Do you want to Generate first {n} Prime Numbers ?\t",end="")
    ch=input()
    if ch in ("yes","YES","Yes","y","Y"):
        gfnp(n)

main()
