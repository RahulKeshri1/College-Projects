#Write a function to determine whether a given natural
#number is a perfect number . A natural number is said
#to be a perfect number if it is the sum of its divisors. For
#example, 6 is a perfect number because 6=1+2+3, but
#15 is not a perfect number because 15≠1+3+5.

def perfect(num):
    ans=0
    li=[]
    for i in range(1,num//2+1):
        if num%i==0:
            ans+=i
            li+=[i]
    
    print("List of Factors:\t",li)
    return ans

def main():
    n=int(input("Enter the number you want to check for perfect number:\t"))
    if n<=0:
        print("Invalid Number")
        return ""
    else:
        ans=perfect(n)
        if ans==0 or ans!=n:
            print("It is not a perfect number.")
        else:
            print("It is a perfect number.")

main()