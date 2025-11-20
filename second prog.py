#find the number of occurance 'bob' in string a consisting of lower case english alphabet 
s='bob'
A="bobob"
c=0
for i in range (0,len(A)):
    if (A[i]=='b' and A[i+1]=='o' and A[i+2]=='b'):
        c=c+1
print(c)