n = int(input())

if n == 1:
    
    print(1)
    
else:

    f,s = 0,0
    
    n -= 1
    
    while n >= 0:
        
        s += (n + ((n-1)*f) + (f+1))
        
        n -= 1
        
        f += 1
        
    print(s)
