s = input()

t = list()

ans = ""

index = 0

for character in "abcdefghijklmnopqrstuvwxyz":
    
    while len(t) > 0 and t[-1] <= character:
        
        ans += t[-1]
        
        t.pop()
        
    pos = s.find(character, index)
    
    while pos >= 0:
        
        while index < pos:
            
            t.append(s[index])
            
            index += 1
            
        ans += character
        
        index += 1
        
        pos = s.find(character, index)
        
while len(t) > 0:
        
    ans += t[-1]
        
    t.pop()
        
print(ans)
