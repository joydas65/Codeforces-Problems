s = input()

vowels = {'a','e','i','o','u','y','A','E','I','O','U','Y'}

ans = ""

for i in s:
    
    if i not in vowels and ord(i) >= 97 and ord(i) <= 122:
        
        ans += "." + i
        
    elif i not in vowels and ord(i) >= 65 and ord(i) <= 90:
        
        ans += "." + chr(ord(i) + 32)
        
print(ans)
