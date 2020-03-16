for _ in range(int(input())):
    
    a,b,n,s = map(int, input().split())
    
    v = (a*n)+b
    
    if v == s:
        print("YES")
        
    elif v < s:
        print("NO")
        
    else:
        x = a*n
        
        if x == s or b == s:
            print("YES")
        elif x < s and b >= (s-x):
            print("YES")
        elif x > s:
            h = s//n
            
            if b >= (s - (h*n)):
                print("YES")
            else:
                print("NO")
