for _ in range(int(input())):
    
    n = int(input())
    
    arr = [[0 for j in range(2*n)] for i in range(2*n)]
    
    row,col,current = 0,0,'#'
    
    for i in range(n):
        
        for j in range(n):
            
            arr[row][col] = current
            arr[row][col+1] = current
            arr[row+1][col] = current
            arr[row+1][col+1] = current
            
            col += 2
            
            if current == '.':
                current = '#'
            else:
                current = '.'
            
        row += 2
        col = 0
        
        if n % 2 == 0:
            if current == '.':
                current = '#'
            else:
                current = '.'
        
    for i in arr:
        for j in i:
            print(j,end="")
        print()
