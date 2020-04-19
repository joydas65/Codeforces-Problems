for _ in range(int(input())):
    
    n = int(input())
    
    arr = []
    
    for i in range(n):
        
        p,c = map(int, input().split())
        
        arr.append((p,c))
        
    flag,plays,clears = 0,0,0
    
    for i,j in enumerate(arr):
        
        if i == 0:
            
            if j[1] > j[0]:
                
                flag = 1
                break
            
            else:
                
                plays,clears = j[0],j[1]
            
        else:
            
            if j[0] < plays or j[1] < clears or j[1] > j[0] or (j[1] > clears and j[0] <= plays):
                
                flag = 1 
                break
            
            elif j[0] >= plays and j[1] >= clears:
                
                if j[1] - clears > j[0] - plays:
                    
                    flag = 1
                    
                    break
            
            plays,clears = j[0],j[1]
        
    if flag == 1:
        
        print("NO")
        
    else:
        
        print("YES")
