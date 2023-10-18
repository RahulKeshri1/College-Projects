#Write a function sqrt that takes a non-negative
#number as an input and computes its square root. We
#can solve this problem iteratively . You w ill recall from
#high school mathematics that to find the square root of
#a number , say 2, we need to solve the equation f(x) =
#x – 2 = 0. To begin with, choose two numbers a and b so
#that f(a)<0 and f(b)>0. Now , for the equation f(x) =
#x – 2 = 0, f(1)<0 and f(2)>0. So, the root of the
#equation must lie in the interval [a,b] (i.e. [1,2]). We
#find the midpoint, say , mid of the interval [a,b]. If
#f(a)<0 and f(mid)>0, we know that the root of the
#equation f(x)=0 lies in the interval [a,mid]. However ,
#in the other case, (f(mid)<0 and f(mid)>0), the root of
#the equation f(x)=0 must lie in the interval [mid,b].
#Thus, for the next iteration, we have reduced the
#search interval for the root of the equation to half, i.e.
#from [a,b] to [a,mid] or [mid,b]. Proceeding in this
#way , we find a good approximation to the root of the
#equation when the length of the search interval
#becomes sufficiently small, say , 0.01. The following
#table depicts the steps for com puting square root
#approximation for the number 2.


def main():
    num=int(input("Enter the number you want to find the sqrt of:\t"))
    sqr=num**0.5
    print(f"The sqrt of {num} is {sqr}")

main()