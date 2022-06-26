for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    maxindex,minindex = 0,0
    
    maxElem,minElem = arr[0],arr[0]
    
    for i,j in enumerate(arr):
        
        if j > maxElem:
            
            maxElem,maxindex = j,i
            
        if j < minElem:
            
            minElem,minindex = j,i
            
    option1 = max(maxindex, minindex)
    option2 = max(n - maxindex, n - minindex)
    
    lb,ub = min(maxindex, minindex),max(maxindex, minindex)
    
    print(min(option2, option1 + 1, lb + 1 + n - ub))
