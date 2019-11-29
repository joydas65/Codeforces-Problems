n,k = map(int, input().split())

arr = list(map(int, input().split()))

score,flag = arr[k-1],0

for i in range(n):
    
    if arr[i] == 0 or arr[i] < score:
        
        flag = 1
        
        break
    
if flag == 1:
    
    print(i)
    
else:
    
    print(n)
