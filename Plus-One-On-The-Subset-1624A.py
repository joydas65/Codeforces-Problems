for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    x,y = min(arr),max(arr)
    
    print(y-x)
