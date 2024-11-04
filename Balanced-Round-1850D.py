for _ in range(int(input())):
    
    n,k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    newArr,c,ans,idx = [],1,0,-1
    
    for i in range(n-1):
        if arr[i+1] - arr[i] <= k:
            c += 1
        else:
            newArr.append(c)
            c = 1
            
    newArr.append(c)
    
    for i,j in enumerate(newArr):
        if ans <= j:
            ans = j
            idx = i
            
    ans = 0
            
    for i,j in enumerate(newArr):
        if i != idx:
            ans += j
            
    print(ans)
    
