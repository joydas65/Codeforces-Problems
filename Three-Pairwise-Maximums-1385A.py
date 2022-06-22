for _ in range(int(input())):
    
    x,y,z = map(int, input().split())
    
    if x == y and y == z:
        
        print("YES")
        print(x,x,x)
        
    elif x == y:
        
        if z <= x:
            
            print("YES")
            print(z,z,x)
            
        else:
            
            print("NO")
            
    elif x == z:
        
        if y <= x:
            
            print("YES")
            print(y,y,x)
            
        else:
            
            print("NO")
            
    elif y == z:
        
        if x <= y:
            
            print("YES")
            print(x,x,y)
            
        else:
            
            print("NO")
            
    else:
        
        print("NO")
