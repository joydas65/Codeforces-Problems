for _ in range(int(input())):
    
    a,k = map(int, input().split())
    
    c = 1
    
    while c < k:
        
        n,minDigit,maxDigit = a,10,0
        
        while n != 0:
            
            minDigit = min(minDigit, n%10)
            maxDigit = max(maxDigit, n%10)
            
            if minDigit == 0:
                break
            
            n //= 10
            
        if minDigit == 0:
            break
        
        a += (minDigit * maxDigit)
        
        c += 1
        
    print(a)
