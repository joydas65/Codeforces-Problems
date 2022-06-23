for _ in range(int(input())):
    
    n = int(input())
        
    arr = list(map(int, input().split()))
    
    left,right,x = 0,n-1,0
    
    while left <= right:
        
        if x % 2 == 0:
            
            print(arr[left],end = " ")
            left += 1
            
        else:
            
            print(arr[right],end = " ")
            right -= 1
            
        x += 1
            
    print()
