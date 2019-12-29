for _ in range(int(input())):
    
    n = int(input())
    
    if n >= 1 and n <= 9:
        
        print(n)
        
    else:
        
        ans,i,d = 9,1,2
        
        while int(str(i)*d) <= n:
            
            ans += 1
            
            i += 1
            
            if i == 10:
                
                i = 1
                d += 1
            
        print(ans)
