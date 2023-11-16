a=int(input("Enter the year:\t"))  
if a%4==0:   
    if a%400==0:
        print("Leap year")
    else:
        a=a%100   
        if a%4==0 and a!=0:
            print("Leap Year")
        else:
            print("Not Leap Year")
else:
    print("Not Leap Year")