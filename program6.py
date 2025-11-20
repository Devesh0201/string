#given an array and find the sum of all sub array
n=int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(i,n+1):
        for k in range(i,j+1):
            print(k , end=" ")
        print()
