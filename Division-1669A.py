for _ in range(int(input())):
    
    n = int(input())
    
    if n <= 1399:
        
        print("Division 4")
        
    elif n >= 1400 and n <= 1599:
        
        print("Division 3")
        
    elif n >= 1600 and n <= 1899:
        
        print("Division 2")
        
    else:
        
        print("Division 1")
