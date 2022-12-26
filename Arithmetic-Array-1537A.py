for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    s = 0
    
    for num in arr:
        
        s += num
        
    if s <= 0 or s < n:
        
        print(1)
        
    elif s == n:
        
        print(0)
        
    else:
        
        print(s-n)
