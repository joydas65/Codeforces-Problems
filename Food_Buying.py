for _ in range(int(input())):
    
    n = int(input())
    
    if n >= 0 and n <= 9:
        
        print(n)
        
    else:
        
        ans = 0
        
        while n >= 10:
            
            ans += ((n//10)*10)
            
            d = n % 10
            
            n = d + (n//10)
            
        print(ans + n)
