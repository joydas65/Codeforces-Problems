n = int(input())

i,ans = 1,0

while i <= n//2:
    
    if (n-i)%i == 0:
        
        ans += 1
        
    i += 1
        
print(ans)
