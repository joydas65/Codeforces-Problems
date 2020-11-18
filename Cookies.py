n = int(input())

arr = list(map(int, input().split()))

s,ans = sum(arr),0

for i,item in enumerate(arr):
    
    if (s - item) % 2 == 0:
        
        ans += 1
        
print(ans)
