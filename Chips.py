n,m = map(int, input().split())

s = (n*(n+1))//2

if s == m:
    
    print(0)
    
elif s > m:
    
    ans = n
    
    while s > m:
        
        s -= ans
        
        ans -= 1
        
    print(m-s)
    
else:
    
    s,i,f = m % s,1,0
    
    while f < s:
        
        f += i
        
        i += 1
        
    if f == s:
        
        print(0)
        
    else:
        
        print(s - (f - i + 1))
