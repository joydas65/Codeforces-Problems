import sys

n,k = map(int, input().split())

arr = []

for _ in range(n):
    
    fi,ti = map(int, input().split())
    
    arr.append((fi,ti))
    
arr,ans = sorted(arr),-sys.maxsize

for item in arr:
    
    if item[1] <= k:
        
        ans = max(ans, item[0])
        
    else:
        
        ans = max(ans, item[0] - (item[1] - k))
        
print(ans)
