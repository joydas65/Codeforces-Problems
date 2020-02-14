x1,y1,x2,y2 = map(int, input().split())

if x1 == x2:
    
    col = abs(y2-y1)
    
    print(x1+col,y1,x2+col,y2)
    
elif y1 == y2:
    
    row = abs(x1-x2)
    
    print(x1,y1+row,x2,y2+row)
    
elif x1 != x2 and y1 != y2:
    
    col = abs(y1-y2)
    row = abs(x1-x2)
    if(row != col):
        
        print(-1)
        
    else:
        
        if y1 < y2:
        
            print(x1,y1+col,x2,y2-col)
            
        else:
            
            print(x1,y1-col,x2,y2+col)
        
        #print(x1,x1+col,x1+row,x1)
