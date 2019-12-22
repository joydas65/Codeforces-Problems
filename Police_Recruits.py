n = int(input())

arr = list(map(int, input().split()))

police,ans = 0,0

for i in arr:
    
    if i == -1 and police == 0:
        
        ans += 1
        
    elif i == -1 and police > 0:
        
        police -= 1
        
    elif i > 0:
        
        if i > 10:
            
            police += 10
            
        else:
        
            police += i
            
print(ans)
