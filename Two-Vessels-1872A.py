for _ in range(int(input())):
    
    a,b,c = map(int, input().split())
    
    diff = abs(a-b)
    
    if a == b:
        print(0)
    elif diff % (2*c) == 0:
        print(diff//(2*c))
    else:
        print(diff//(2*c) + 1)
