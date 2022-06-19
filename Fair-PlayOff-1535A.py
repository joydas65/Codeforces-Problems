for _ in range(int(input())):
    
    a,b,c,d = map(int, input().split())
    
    x,y = max(a,b),max(c,d)
    
    max1 = max(a,b,c,d)
    
    max2 = max(b,c,d) if max1 == a else max(a,c,d) if max1 == b else max(a,b,d) if max1 == c else max(a,b,c)
    
    if max2 == y or max2 == x:
        
        print("YES")
        
    else:
        
        print("NO")
