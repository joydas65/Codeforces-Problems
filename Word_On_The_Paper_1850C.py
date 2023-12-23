for _ in range(int(input())):
    
    arr,ans = [],""
    
    for i in range(8):
        
        arr.append(input())
        
    for i,j in enumerate(arr):
        
        for k,x in enumerate(j):
            
            if ord(x) >= 97 and ord(x) <= 122:
                
                ans = x
                
                break
            
        if ans != "":
            break
        
    i += 1
            
    while i < 8 and ord(arr[i][k]) >= 97 and ord(arr[i][k]) <= 122:
        
        ans += arr[i][k]
        
        i += 1
        
    print(ans)
        
        
