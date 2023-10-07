#_____________________________________________________________________________________
#   Write a Program to find roots of quadratic equation.
#_____________________________________________________________________________________

#   Function to calculate roots of the quadratic equation.
def compute(a,b,c):
    d=(b**2 - 4*a*c)
    if d<0:
        print("This equation has no solutions as its descriminant is negative.")
        return " "
    elif a==0:
        print("This equation is not a Quadratic Equation.")
        return " "
    else:
        ans1=((-b)+(d**0.5))/(2*a)
        ans2=((-b)-(d**0.5))/(2*a)
        if ans1==ans2:
            print(f"This equation has two solutions which are numerically equal, i.e.\t{ans1}")
            return ""
        else:
            print(f"This equation has two solutions:\n First solution:-\t {ans1} \n and Second solutions:-\t {ans2}.")
            return ""

#   Main Function 
def main():
    ch='y'
    while ch in ("yes","YES","Yes","y","Y"):
        a=int(input("Enter the co-efficient of x^2 :\t"))
        b=int(input("Enter the co-efficient of x:\t"))
        c=int(input("Enter the constant:\t"))
        print(f"The equation formed is {a}x^2+({b})x+({c})=0")
        op=input("Is this equation correct?(y/n):\t")
        if op in ("yes","YES","Yes","y","Y"):
            compute(a,b,c)
            ch=input("\n Do you want to calculate the roots of another equation(s)?:\t")
            if ch in ("yes","YES","Yes","y","Y"):
                continue
            else:
                break
        else:
            print("Do you want to re-enter the co-efficients?:\t")
            ch=input()
            if ch in ("yes","YES","Yes","y","Y"):
                continue

    print("Thank you for your valuable time:)")

main()