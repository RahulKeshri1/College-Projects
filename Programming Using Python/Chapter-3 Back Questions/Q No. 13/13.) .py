#Write a function to multiply two non-negative
#numbers by repeated addition, for example, 7*5 = 7 +
#7 + 7 + 7 + 7.

def calculate(num1,num2):
    result=0
    print(num1,end="")
    for i in range(num2):
        result=result+num1
        if i==num2-1:
            print()
            break
        print(f" + {num1}",end="")
    return result
def main():
    n1=int(input("Enter the Number you want to Multiply to:\t"))
    n2=int(input("Enter the Number you want to Multiply:\t"))
    ans=calculate(n1,n2)
    print("The ans is:=",ans)

main()