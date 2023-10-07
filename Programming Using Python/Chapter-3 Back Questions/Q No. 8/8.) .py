#Write a function that returns True or False depending
#on whether the given number is a palindrome.

def pallindrome(x):
    real=x
    result=0
    while x>0:
        rem=x%10
        result=result*10+rem
        x=x//10
    if real==result:
        return True
    else:
        return False
    
def main():
    num=int(input("Enter the number you want to check for Pallindrome:\t"))
    print(pallindrome(num))

main()