r,c = map(int, input().split())

arr,flag,ans = [],0,0

for _ in range(r):
    
    arr.append(list(input()))
    
for i in range(r):
    
    for j in range(c):
        
        if arr[i][j] == 'S':
            
            flag = 1
            
            break
        
    if flag == 0:
        
        for j in range(c):
            
            if arr[i][j] == '.':
            
                arr[i][j] = 'E'
                
                ans += 1
                
    flag = 0
    
flag = 0
    
for i in range(c):
    
    for j in range(r):
        
        if arr[j][i] == 'S':
            
            flag = 1
            
            break
        
    if flag == 0:
        
        for j in range(r):
            
            if arr[j][i] == '.':
                
                ans += 1
                
                arr[j][i] = 'E'
                
    flag = 0
                
print(ans)
