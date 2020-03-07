for _ in range(int(input())):
    
    b,p,f = map(int, input().split())
    
    h,c = map(int, input().split())
    
    buns = b // 2
    
    if buns >= (p + f):
        
        print((p*h)+(f*c))
        
    else:
        
        hamburger = min(p, buns)
        
        chickenburger = buns - hamburger
        
        Chicken,ans = min(f, buns),0
        
        while hamburger >= (buns - Chicken) and chickenburger <= Chicken:
            
            ans = max(ans, (hamburger * h) + (chickenburger * c))
            
            hamburger -= 1
            
            chickenburger += 1
            
        print(ans)
