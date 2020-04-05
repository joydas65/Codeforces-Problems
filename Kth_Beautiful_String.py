arr = []

c,i,h = 1,1,0

while i <= 10**5:
    
    arr.append(c)
    
    i += 1
    
    c += i
    
    h += 1

for _ in range(int(input())):
    
    n,k = map(int, input().split())
    
    lb,ub,flag = 0,h-1,0
    
    while lb <= ub:
        
        mid = (lb + ub)//2
        
        if arr[mid] == k:
            
            flag = 1
            break
        
        elif arr[mid] > k:
            
            ub = mid - 1
            
        else:
            
            lb = mid + 1
            
    pos = 0
            
    if flag == 1:
        
        pos = mid + 2
        
    else:
        
        pos = lb + 2
    
    #print(pos)
    
    ones = n - 2
    
    print("a"*(n - pos) + "b" + "a"*(arr[pos-2] - k) + "b" + "a"*(ones-((n-pos)+(arr[pos-2]-k))))
