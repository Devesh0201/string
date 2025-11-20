s=input("enter the word : ")
vowel = 0
const = 0
for i in range(len(s)):
    if (s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u"):
        vowel+=1
    else:
        const+=1
print("vowel",vowel)
print("const",const)
        