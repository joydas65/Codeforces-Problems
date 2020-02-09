n,k = map(int, input().split())

heights = list(map(int, input().split()))

s = 0

for i in range(k):
    
    s += heights[i]
    
ans,prev = 0,s
    
for i in range(k,n):
    
    s += heights[i]
    s -= heights[i-k]
    
    if s < prev:
        
        ans = i - k + 1
        
        prev = s
    
print(ans+1)
