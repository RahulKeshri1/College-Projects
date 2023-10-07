def table(x,y):
    for i in range(x,y+1):
        for j in range(1,11):
            print(i*j)
        print()
def main():
    x=int(input("Enter the first number of the range:\t"))
    y=int(input("Enter the second number of the range:\t"))
    table(x,y)
    input()
main()