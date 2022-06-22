for _ in range(int(input())):
    
    n,x = map(int, input().split())
    
    if n <= 2:
        
        print(1)
        
    elif x == 1:
        
        print(n - 1)
        
    else:
        
        ans = 1
        
        floor,flag = 2,0
        
        while flag == 0:
            
            if floor + x < n:
                
                ans += 1
                
            else:
                
                flag = 1
                
                break
            
            floor += x
            
        print(ans + 1)
