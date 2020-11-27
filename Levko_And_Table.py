n,k = map(int, input().split())

arr = [[0 for j in range(n)] for i in range(n)]

col = n-1

for i in range(n):
    
    for j in range(n):
        
        arr[i][j] = k-(n-1) if j == col else 1
        
    col -= 1
        
for item in arr:
    
    for i in item:
        
        print(i,end = " ")
        
    print()
