for _ in range(int(input())):
    
    a,b,c = map(int, input().split())
    
    mx = 0
    
    for i in range(5):
        
        mx = max((a+1)*b*c, a*(b+1)*c, a*b*(c+1))
        
        if mx == (a+1)*b*c:
            a += 1
        elif mx == (b+1)*a*c:
            b += 1
        else:
            c += 1
            
    print(mx)
