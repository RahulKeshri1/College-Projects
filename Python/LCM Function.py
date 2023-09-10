#Function to calculate LCM.
def compute_lcm(num1,num2):

    if(num1 > num2):
        greater=num1
    else:
        greater=num2

    while True:
        if(greater % num1==0 and greater % num2==0):
            LCM=greater
            break
        else:
            greater+=1

    return LCM
