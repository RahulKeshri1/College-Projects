# Write a function that takes two numbers as input
#parameters and returns their least common multiple.

def lcm(num1,num2):
    for i in range(num1,num1*num2):
        if i%num1==0 and i%num2==0:
            return i
    
    return num1*num2

def main():
    s=int(input("Enter the First number:\t"))
    r=int(input("Enter the Second number:\t"))
    ans=lcm(s,r)
    print(f"The LCM of {s} and {r}:\t",ans)
    input()

main()