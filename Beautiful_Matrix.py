arr = []

for i in range(5):
    
    x = list(map(int, input().split()))
    
    arr.append(x)
    
row,col,flag = 0,0,0
    
for i in arr:
    
    for j in i:
        
        if j == 1:
            
            flag = 1
            
            break
        
        col += 1
        
    if flag == 1:
        
        break
        
    row += 1
    
    col = 0
    
print(abs(row-2) + abs(col - 2))
