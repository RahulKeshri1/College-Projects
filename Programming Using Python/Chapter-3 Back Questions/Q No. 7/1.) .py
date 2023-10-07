#Wr ite a function that finds the sum of the n terms of
#the following series:
#1 . 1 – x^2 /2! + x^4 /4! – x^6 /6! + … x^n /n!
def factorial(n):
    ans=1
    if n==0 or n==1:
        return ans
    for i in range(1,n+1):
        ans=ans*i

    return ans

def summation(x,n):
    ans=1
    for i in range(2,n+1,2):
        if (i/2)%2==0:
            ans=ans+(pow(x,i))/(factorial(i))
        else:
            ans=ans-(pow(x,i))/(factorial(i))
    return ans

def main():
    number=int(input("Enter the value of x:\t"))
    n=int(input("Enter the Last Power(multiple of 2):\t"))
    if n%2!=0:
        print("Entered number is not the multiple of 2.")
        return ""
    else:
        ans=summation(number,n)
        print("The sum of the series:\t",ans)
    
main()