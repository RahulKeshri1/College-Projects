#__________________________________________________________________________________________
#   Write a function that prints a dictionary where the keys are numbers between 1 and 5
#   and the values are cubes of the keys.
#__________________________________________________________________________________________
def dic(nth):
    dict={}
    for i in range(1,nth+1):
        dict[i]=i**3

    return dict

def main():
    n=int(input("Enter the last range of the dictionary:\t"))
    dict=dic(n)
    ch=input("Do you want to search for a value?(y/n)")
    if ch in ('yes','y','Yes','YES','Y'):
        num=int(input("Enter the key value :\t"))
        if num>n:
            print("Key Value is out of range")
        else:
            print(f"The value of the key entered:\t{dict[num]}")
    ch=input("Do you want to print the whole dictionary?(y/n)")
    if ch in ('yes','y','Yes','YES','Y'):
        print(dict)
main()