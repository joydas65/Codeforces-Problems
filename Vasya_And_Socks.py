n,m = map(int, input().split())

ans = 0

while n > 0:
    
    if n < m:
        
        ans += n
        
    else:
        
        ans += m
        
    n -= (m-1)
    
print(ans)
