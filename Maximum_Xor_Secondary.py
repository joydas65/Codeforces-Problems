n = int(input())

arr = list(map(int, input().split()))

s = []

ans = 0

for i in range(n):
    
    while s != []:
        
        ans = max(ans,arr[i]^s[-1])
        
        if arr[i] < s[-1]:
            
            break
            
        else:
            
            s.pop()
            
    s.append(arr[i])
    
print(ans)
