n = int(input())

matrix,flag = [],0

for i in range(n):
    
    matrix.append(list(input()))
    
for i in range(n):
    
    for j in range(n):
        
        if matrix[i][j] == '.':
            
            if i+1 < n and j-1 >= 0 and matrix[i+1][j-1] == '.' and matrix[i+1][j] == '.' and j+1 < n and matrix[i+1][j+1] == '.' and i+2 < n and matrix[i+2][j] == '.':
                
                matrix[i][j],matrix[i+1][j-1],matrix[i+1][j],matrix[i+1][j+1],matrix[i+2][j] = '#','#','#','#','#'
                
            else:
                
                flag = 1
                
                break
                
    if flag == 1:
        
        break
        
if flag == 1:
    
    print("NO")
    
else:
    
    print("YES")
                
                
        
