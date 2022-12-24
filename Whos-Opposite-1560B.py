for _ in range(int(input())):
    
    a,b,c = map(int, input().split())
    
    if abs(a-b) == 1:
        print(-1)
    else:
        diff = abs(a-b)
        
        maxval = 2 * diff
        
        if a > maxval or b > maxval or c > maxval:
            print(-1)
        else:
            if c+diff <= maxval:
                print(c+diff)
            elif c-diff >= 1:
                print(c-diff)
            else:
                print(-1)
