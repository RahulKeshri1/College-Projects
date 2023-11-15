#_____________________________________________________________________________________
#   Write a Program to read a file and
#       a) Print the total numbers of characters, words and lines in the file.
#       b) Calculate the frequency of each character in the file. Use a variable of 
#          dictionary type to maintain the count.
#       c) Print the words in reverse order.
#       d) Copy even lines of the file to a file named "File1" and odd lines to another
#          file named "File2".
#_____________________________________________________________________________________

#Function to count the number of characters in a string.
def characters(str):
    return len(str)

#Function to count the no. of Words.    
def words(str):
    count=0
    l=str.split()
    for ch in l:
        count+=1
    return count

#Function to count the no. of lines.
def lines(str):
    count=0
    for i in range(len(str)):
        if str[i]=='\n':
            count+=1
    return count

#Function to Calculate the frequency of each character in the file
def frequency(str):
    dic={}
    for i in range(len(str)):
        if str[i] in dic:
            dic[str[i]]+=1
        else:
            dic[str[i]]=1
    return dic

#Function to Reverse the words and then Print 
def reverse(str):
    l=str.split()
    ans=""
    for j in range(len(l)-1,-1,-1):
        ans+=l[j]+" "
    return ans

#Function to Distribute even lines to File1 and odd lines to File2.
def oddeven(filo,file1,file2,n):
    filo.seek(0)
    for i in range(1,n+1):
        if i%2!=0:
            file2.writelines(filo.readline())
        else:
            file1.writelines(filo.readline())

def main():
    filo=open("C:/Users/rahul/OneDrive/Desktop/File.txt")
    str=filo.read()
    
    
    print("No. of characters in the file:\t",characters(str))
    
    print("No. of Words:\t",words(str))
    
    print("No. of Lines",lines(str))
    
    dictionary=frequency(str)
    for key,value in dictionary.items():
        print(key,"is present",value,"times")
    
    print("After reversing the words of the file:\t",reverse(str))
    
    file1=open("C:/Users/rahul/OneDrive/Desktop/File1.txt","w")
    file2=open("C:/Users/rahul/OneDrive/Desktop/File2.txt","w")
    oddeven(filo,file1,file2,lines(str))
    filo.close()
    file1.close()
    file2.close()
main()