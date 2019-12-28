n,m = map(int, input().split())

ans = 0

if n >= m:
    
    print(n-m)
    
else:
    
    if m % 2 == 1:
        
        ans = 1
        
        m += 1
        
    while m > n:
        
        if m % 2 == 0:
        
            m //= 2
            ans += 1
            
        else:
            
            m = (m+1)//2
            ans += 2
            
    print(ans + n - m)
