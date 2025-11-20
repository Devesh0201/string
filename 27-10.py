# given an array and find the sum of all sub array 
ans=0
a=[3,-1,4]
n=len(a)
for i in range(0,n):
    sum =0
    for j in range(i,n):
        sum+=a[j]
        ans+=sum
print(ans)



3*3+(-1)*4+4*3
#if we know in how many sub array eaxh element is coming we can solve this problem faster 
# in how many subarray index 3 is coming 
a=[3,-2,4,-1,2,6]
