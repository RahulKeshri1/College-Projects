#Write a program that prints Armstrong numbers in
#the range 1 to 1,000. An Armstrong number is a
#number whose sum of the cubes of the digits is equal to
#the number itself. For example, 370 = 3^3 + 7^3 + 0^3 .

def armstrong(x):
    real=x
    result=0
    while x>0:
        rem=x%10
        result+=rem**3
        x=x//10
    if real==result:
        return True
    else:
        return False


def main():
    #num=int(input("Enter the number you want to check for Armstrong:\t"))
    for i in range(1,1001):
        if armstrong(i):
            print(i)


main()