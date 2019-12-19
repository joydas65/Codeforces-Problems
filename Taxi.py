n = int(input())

arr = list(map(int, input().split()))

d = dict()

for i in arr:
    
    if i in d:
        
        d[i] += 1
        
    else:
        
        d[i] = 1
        
ans = 0

#print(d)
        
for i in arr:
    
    if i == 4:
        
        ans += 1
        
    elif i == 3 and d[i] >= 1:
        
        if 1 in d and d[1] >= 1:
            
            d[3] -= 1
            
            d[1] -= 1
            
        else:
            
            d[3] -= 1
            
        ans += 1
        
    elif i == 2 and d[i] >= 1:
        
        if d[i]-1 >= 1:
            
            d[i] -= 2
            
        elif 1 in d and d[1] >= 2:
            
            d[i] -= 1
            
            d[1] -= 2
            
        elif 1 in d and d[1] >= 1:
            
            d[i] -= 1
            
            d[1] -= 1
            
        else:
            
            d[i] -= 1
            
        ans += 1
        
    elif i == 1 and d[i] >= 1:
        
        if 3 in d and d[3] >= 1:
            
            d[3] -= 1
            
            d[i] -= 1
            
        elif 2 in d and d[2] >= 1 and d[1]-1 >= 1:
            
            d[2] -= 1
            
            d[1] -= 2
            
        elif 2 in d and d[2] >= 1 and d[1] >= 1:
            
            d[2] -= 1
            
            d[1] -= 1
        
        elif d[i] >= 4:
            
            d[i] -= 4
            
        elif d[i] >= 3:
            
            d[i] -= 3
            
        elif d[i] >= 2:
            
            d[i] -= 2
            
        elif d[i] >= 1:
            
            d[i] -= 1
            
        ans += 1
        
    #print(d)
        
print(ans)
