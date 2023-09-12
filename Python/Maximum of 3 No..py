#Write a program in Python to create a function of Maximum of two number

def maximum(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2
    
    
def main():
    a=int(input("Enter First number:\t"))   
    b=int(input("Enter Second number:\t"))
    max=maximum(a,b)
    print("Maximum among",a,",",b,"is:",max)

main()