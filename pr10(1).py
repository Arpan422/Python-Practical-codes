def isPalindrome (s):
    return s==s[::-1]
s="malayalam"
print(s)
ans=isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")