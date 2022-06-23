for _ in range(int(input())):
    
    n = int(input())
        
    arr = list(map(int, input().split()))
    
    even,odd = 0,0
    
    for item in arr:
        
        if item % 2 == 0:
            
            even += 1
            
        else:
            
            odd += 1
            
    print("Yes" if even == odd else "No")
