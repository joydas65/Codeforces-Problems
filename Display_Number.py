for _ in range(int(input())):
    
    x = int(input())
    
    if x % 2 == 0:
        
        print("1"*(x//2))
        
    else:
        
        print("7"*1 + "1"*((x-3)//2))
