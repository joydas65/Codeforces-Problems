i = 1

arr,ans,pow2 = [],["Sheldon","Leonard","Penny","Rajesh","Howard"],[]

n = int(input())

if n <= 5:
    
    print(ans[n-1])
    
else:

    s,x = 0,10**9
    
    while s <= x:
        
        pow2.append(i)
        
        s += (5*i)
        arr.append(s)
        
        i = i * 2
        
    pow2.append(i)
    
    arr.append(s)
    
    #print(len(pow2),len(arr))
        
    #print(pow2)
    
    lb,ub,flag = 0,len(arr)-1,0
    
    while lb <= ub:
        
        mid = (lb + ub)//2
        
        if arr[mid] == n:
            
            flag = 1
            
            break
        
        elif arr[mid] < n:
            
            lb = mid + 1
            
        else:
            
            ub = mid - 1
            
    #print(lb,arr)
        
    if flag == 1:
        
        print("Howard")
            
    else:
        p = pow2[lb]
        v = n - arr[ub]
        
        #print(v)
        
        if v % p == 0:
            
            print(ans[((v//p)-1)%5])
            
        else:
            
            print(ans[(v//p)%5])
