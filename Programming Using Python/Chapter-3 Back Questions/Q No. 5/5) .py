#Write a function that takes two numbers as input
#parameters and returns their greatest common
#divisor .

def hcf(num1,num2):
    ans=0
    for i in range(1,max(num1//2,num2//2)):
        if num1%i==0 and num2%i==0:
            ans=i
    return ans
def main():
    n1=int(input("Enter the first number:\t"))
    n2=int(input("Enter the second number:\t"))
    ans=hcf(n1,n2)
    print("Greatest Common Divisor=\t",ans)

main()