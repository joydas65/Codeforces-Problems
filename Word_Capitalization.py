s = input()

if ord(s[0]) >= 65 and ord(s[0]) <= 90:
    
    print(s)
    
else:
    
    print(chr(ord(s[0]) - 32) + s[1:])
