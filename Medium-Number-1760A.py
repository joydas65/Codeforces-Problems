for _ in range(int(input())):
    
    a,b,c = map(int, input().split())
    
    mx,mn = max(a,b,c),min(a,b,c)
    
    print((a+b+c)-(mx+mn))
