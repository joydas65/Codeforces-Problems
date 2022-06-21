for _ in range(int(input())):
    
    n = int(input())
    
    s = input()
    
    c = 0
    
    for item in s:
        
        if item == '(':
            
            c += 1
            
        else:
            
            c = max(c - 1, 0)
            
    print(c)
