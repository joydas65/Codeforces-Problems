n,k = map(int, input().split())

arr = list(map(int, input().split()))

arr = sorted(arr)

i,ans = 2,0

while i < n:
    
    if arr[i]+k <= 5:
        
        ans += 1
        
    i += 3
    
print(ans)
