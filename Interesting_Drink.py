n = int(input())

arr = list(map(int, input().split()))
n = len(arr)
arr = sorted(arr)

for _ in range(int(input())):
    
    x = int(input())
    
    lb,ub = 0,n-1
    
    while lb <= ub:
        
        mid = (lb + ub)//2
        
        if arr[mid] == x:
            
            lb = mid + 1
            
        elif x < arr[mid]:
            
            ub = mid - 1
            
        else:
            
            lb = mid + 1
            
    print(ub + 1)
