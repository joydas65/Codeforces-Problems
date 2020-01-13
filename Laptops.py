arr,c,flag = [],0,0

for _ in range(int(input())):
    
    a,b = map(int, input().split())
    
    arr.append((a,b))
    
    c += 1
    
if c == 1:
    
    print("Poor Alex")
    
else:
    
    arr = sorted(arr, key = lambda x : x[1])
    
    if arr[0][0] > arr[1][0]:
        
        print("Happy Alex")
        
    else:
        
        price,flag = max(arr[0][0],arr[1][0]),0
        
        for i in range(2,c):
            
            if price > arr[i][0]:
                flag = 1
                
                break
            price = max(price, arr[i][0])
        if flag == 1:
            print("Happy Alex")
            
        else:
            print("Poor Alex")
