for _ in range(int(input())):
    
    n,k = map(int, input().split())
    
    ans = 0
    
    if n <= k:
        
        print(k//n if k%n == 0 else k//n + 1)
        
    else:
        
        if n%k == 0:
            print(1)
        else:
            print(2)
