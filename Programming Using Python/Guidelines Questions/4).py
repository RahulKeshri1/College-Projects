#_____________________________________________________________________________________________________________
#   Write a Program to accepts a character and perform the following:
#       a. Print whether the character is a letter or a numeric digit or a special character.
#       b. If the character is a letter, print whether the letter is in uppercase or lowercase.
#       c. If the chcaracter is a numeric digit, print its name in text(eg.,if input is 9, output is NINE.)
#_____________________________________________________________________________________________________________

#Function to convert Numbers into their Number Names.
def inttowords(num):
    words ={
        0:"ZERO",
        1:"ONE",
        2:"TWO",
        3:"THREE",
        4:"FOUR",
        5:"FIVE",
        6:"SIX",
        7:"SEVEN",
        8:"EIGHT",
        9:"NINE"
    }
    num=int(num)
    number=0
    ans=" "
    while num>0:
        rem=num%10
        num//=10
        number=number*10+rem
    while number>0:
        num=number%10
        ans=ans+words[num]+" "
        number//=10
    return ans

#Function to Check a character whether it is letter,number,special character. 
def check(char):
    if char>='A' and char<='Z':
        print(char,"is a letter.")
        print(char,"is in Uppercase.")
        return ""
    elif char>='a' and char<='z':
        print(char,"is a letter.")
        print(char,"is in Lowercase.")
        return ""
    elif char>='0' and char<='9':
        print(char,"is a Numeric Digit.")
        print(char,"is",inttowords(char))
    else:
        print(char,"is a Special Character.")

#Main Function
def main():
    ch=input("Enter a character:\t")
    check(ch)

main()