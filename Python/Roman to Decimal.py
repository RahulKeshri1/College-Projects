m={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
ans=0
num=input("Enter the number in Roman Numerals:\t")
for i in range(len(num)):
    if i==len(num)-1:
        ans+=m[num[i]]
    elif m[num[i]]<m[num[i+1]]:
        ans-=m[num[i]]
    else:
        ans+=m[num[i]]
print("Number in Decimal:\t",ans)