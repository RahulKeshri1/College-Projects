#_____________________________________________________________________________________
#   Write a Program to perform following operations on a string:
#       a) Find the frequency of a character in a string.
#       b) Replace a character by another character in a string.
#       c) Remove the first occurence of a character from a string.
#       d) Remove all occurence of a character from a string.
#_____________________________________________________________________________________
 
#   Function to display the frequency of a character in a string.
def frequency(string,character):
    counter=0
    for i in range(len(string)):
        if character==string[i]:
            counter+=1
    return counter


def main():
    st=input("Enter the string in which you want to perform the string operations:\t")
    
    #   a) Find the frequency of a character in a string.
    ch=input("Do you want to find the frequency of a character in a string?\t")
    if ch in ("yes","YES","Yes","y","Y"):
        op=input("Enter the character you want to find the frequency of:\t")
        ans=frequency(st,op)
        print(f"{op} is present {ans} time(s) in '{st}'")

    #   b) Replace a character by another character in a string.
    ch=input("Do you want to replace a character in the string?\t")
    if ch in ("yes","YES","Yes","y","Y"):
        fr=input("Enter the character you want to replace :\t")
        to=input("Enter the character you want to be placed:\t")
        prev=st
        st=st.replace(fr,to)
        print(f"Previous string was '{prev}' and after replacing '{fr}' from '{to}' is '{st}' :)")

    #   c) Remove the first occurence of a character from a string.
    ch=input("Do you want to remove the first occurrence in the string:\t")
    if ch in ("yes","YES","Yes","y","Y"):
        fr=input("Enter the character you want remove the first occurrence:\t")
        if fr in st:
            ans=st.replace(fr,"",1)
            print(f"Previous string was '{st}' and after removing '{fr}' the string is '{ans}' :)")
        else:
            print(f"'{fr}' is not present in the string:-  '{st}'")
    
    #   d) Remove all occurence of a character from a string.
    ch=input("Do you want to remove all occurrence of a letter in the string:\t")
    if ch in ("yes","YES","Yes","y","Y"):
        fr=input("Enter the character you want remove all occurrences:\t")
        if fr in st:
            ans=st.replace(fr,"")
            print(f"Previous string was '{st}' and after removing '{fr}' the string is '{ans}' :)")
        else:
            print(f"'{fr}' is not present in the string:-  '{st}'")

main()