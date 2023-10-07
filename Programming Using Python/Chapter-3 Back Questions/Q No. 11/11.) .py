# Write a function that takes two numbers as input
#parameters and returns True or False depending on
#whether they are co-primes. Two numbers are said to
#be co-prime if they do not hav eany common divisor
#other than one.

def factors(num):
    l=[]
    for i in range(1,num//2+1):
        if num%i==0:
            l+=[i]
    return l

def compare(num1,num2):
    factor1=factors(num1)
    factor2=factors(num2)
    n=min(len(factor1),len(factor2))
    for i in range(n):
        for j in range(n):
            if factor1[i]==1 or factor2==1:
                continue
            if factor1[i]==factor2[j]:
                return False
    return True

def main():
    num1=int(input("Enter the First Number:\t"))
    num2=int(input("Enter the Second Number:\t"))

    if compare(num1,num2):
        print(f"{num1} and {num2} are Co-primes.")
    else :
        print(f"{num1} and {num2} are not Co-primes.")

main()