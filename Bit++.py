ans = 0

for _ in range(int(input())):
    
    s = input()
    
    if s[0] == '+' or '+' in s:
        
        ans += 1
        
    elif s[0] == '-' or '-' in s:
        
        ans -= 1
        
print(ans)
