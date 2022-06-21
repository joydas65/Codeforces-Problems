for _ in range(int(input())):
    
    n,k = map(int, input().split())
    
    if k < n:
        
        print(k)
        
    else:
    
        val1 = k // (n - 1)
        
        val2 = n * val1
        
        if k % (n - 1) == 0:
            
            print(val2 - 1)
            
        else:
            
            print(val2 + (k % (n - 1)))
