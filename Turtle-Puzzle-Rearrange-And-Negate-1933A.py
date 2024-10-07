for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    ans = 0
    
    for i,j in enumerate(arr):
        
        if j < 0:
            ans += abs(j)
        else:
            ans += j
            
    print(ans)
