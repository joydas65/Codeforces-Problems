for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    minimum,ans = min(arr),0
    
    for num in arr:
        
        ans += (num - minimum)
        
    print(ans)
