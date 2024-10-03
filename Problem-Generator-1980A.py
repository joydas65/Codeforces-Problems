for _ in range(int(input())):
    
    n,m = map(int, input().split())
    
    problems = input()
    
    d,ans = dict(),0
    
    for i in problems:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
            
    for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        if i in d:
            if d[i] < m:
                ans += (m-d[i])
        else:
            ans += m
            
    print(ans)
