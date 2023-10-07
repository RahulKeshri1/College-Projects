#Wr ite a function that finds the sum of the n terms of
#the following series:
#2. e^x=1 + x^2 /1! + x^2 /2! + x^3 /3! + … x^n /n!

def factorial(n):
    ans=1
    if n==0 or n==1:
        return ans
    for i in range(1,n+1):
        ans=ans*i

    return ans


def summation(x):
    ans=1
    n=1000
    for i in range(1,n):
            ans=ans+(pow(x,i))/(factorial(i))
    
    return ans

def main():
     x=int(input("Enter the power of e:\t"))
     ans=summation(x)
     print(f"Value of e^{x}={ans}")
     return ""

main()