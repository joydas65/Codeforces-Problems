for _ in range(int(input())):
    
    w,h,n = map(int, input().split())
    
    if w % 2 == 1 and h % 2 == 1:
        
        print("YES" if n == 1 else "NO")
        
    elif n == 1:
        
        print("YES")
        
    else:
        
        tempW,tempH = w,h
        
        while w % 2 == 0:
            
            w //= 2
            
        while h % 2 == 0:
            
            h //= 2
            
        if w != tempW and h != tempH:
            
            print("YES" if ((tempW // w) * (tempH // h)) >= n else "NO")
            
        elif w != tempW:
            
            print("YES" if (tempW // w) >= n else "NO")
            
        elif h != tempH:
            
            print("YES" if (tempH // h) >= n else "NO")
            
        else:
            
            print("NO")
