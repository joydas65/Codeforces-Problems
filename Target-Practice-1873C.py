score = [[0 for j in range(10)] for i in range(10)]

for x in range(1,6):
    
    for i in range(x-1,11-x):
        score[x-1][i] = x
        
    for i in range(x-1,11-x):
        score[i][x-1] = x
        
    for i in range(x-1,11-x):
        score[10-x][i] = x
        
    for i in range(x-1,11-x):
        score[i][10-x] = x
        
for _ in range(int(input())):

    arr = []
    for i in range(10):
    
        arr.append(list(input()))
        
    total_score = 0
        
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 'X':
                total_score += score[i][j]
                
    print(total_score)
