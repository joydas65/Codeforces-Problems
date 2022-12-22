for _ in range(int(input())):
    
    a,b,c = map(int, input().split())
    
    t1 = abs(a-1)
    
    t2 = abs(b-c) + abs(c-1)
    
    if t1 == t2:
        print(3)
    elif t1 < t2:
        print(1)
    else:
        print(2)
