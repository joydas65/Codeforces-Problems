n,m = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0]*n

dp[-1],seen = 1,set()
seen.add(arr[-1])

for i in range(n-2,-1,-1):
    
    if arr[i] not in seen:
        
        seen.add(arr[i])
        
        dp[i] = dp[i+1] + 1
        
    else:
        
        dp[i] = dp[i+1]

for _ in range(m):
    
    q = int(input())
    
    print(dp[q-1])
