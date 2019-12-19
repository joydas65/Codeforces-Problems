n,a,b,c = map(int, input().split())

arr = [0 for i in range(n+1)]

for i in range(1,n+1):
    
    v1,v2,v3 = 0,0,0
    
    if i-a >= 0:
        
        if i == a or arr[i-a] > 0:
        
            v1 = 1 + arr[i-a]
        
    if i-b >= 0:
        
        if i == b or arr[i-b] > 0:
        
            v2 = 1 + arr[i-b]
        
    if i-c >= 0:
        
        if i == c or arr[i-c] > 0:
        
            v3 = 1 + arr[i-c]
        
    arr[i] = max(v1,v2,v3)
    
print(arr[-1])

#print(arr)
