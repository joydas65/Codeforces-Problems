for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    seen,found = set(),0
    
    for num in arr:
        
        if num in seen:
            found = 1
            break
        
        seen.add(num)
        
    print("YES" if found == 0 else "NO")
