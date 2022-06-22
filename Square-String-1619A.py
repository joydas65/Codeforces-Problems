for _ in range(int(input())):
    
    s = input()
            
    n = len(s)
    
    if n % 2 == 1:
        
        print("NO")
        
    else:
        
        x = 0
        
        while x < (n // 2):
            
            if (s[:x+1] * 2) == s:
                
                print("YES")
                break
            
            x += 1
            
        if x == (n // 2):
            
            print("NO")
