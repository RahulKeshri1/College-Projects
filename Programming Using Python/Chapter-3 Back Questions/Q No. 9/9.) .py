#Write a function that returns the sum of digits of a
#number , passed to it as an argument.

def sum_of_digits(x):
    result=0
    while x>0:
        rem=x%10
        result=result+rem
        x=x//10
    return result

def main():
    num=int(input("Enter the number for which you want to find the sum of it's digits:\t"))
    ans=sum_of_digits(num)
    print(f"Sum of the digits of {num} = {ans}")

main()