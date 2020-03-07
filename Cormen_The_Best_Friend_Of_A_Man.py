n,k = map(int, input().split())

arr = list(map(int, input().split()))

ans = 0

for i,j in enumerate(arr):
    
    if i >= 1:
        
        if j + arr[i-1] < k:
            
            ans += (k - (arr[i-1] + j))
            
            arr[i] += (k - (arr[i-1] + j))
            
print(ans)

for i in arr:
    
    print(i,end = " ")
    
print()
