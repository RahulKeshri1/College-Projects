#_____________________________________________________________________________________________________
#   Write a function that accepts two strings and returns the indices of all occurrences of 
#   the second string in the first string as a list. If the second string is not present in the first
#   string then it should return -1
#_____________________________________________________________________________________________________

def indices(string1,string2):
    print("\n List indicating the positions of each letter of First String in the Second String.")
    for i in range(len(string1)):
        l1=[]
        for j in range(len(string2)):
            if string1[i]==string2[j]:
                l1=l1+[j] 
        if len(l1)==0:
            l1=[-1]   
        print(f"'{string1[i]}' is present at:-{l1} Position(s).")
    



def main():
    string1=input("Enter the First String:\t\t")
    string2=input("Enter the Second String:\t")
    indices(string1,string2)

main()