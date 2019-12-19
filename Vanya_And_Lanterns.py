import sys

n,l = map(int, input().split())

l = float(l)

arr = list(map(int, input().split()))

arr = sorted(arr)

lb,ub,ans,prevlb,prevub = 0,l,sys.maxsize,0,0

while lb < ub:
    
    prevlb,prevub = lb,ub
    
    mid,flag = (lb + ub)/2,0
    
    if arr[0] - mid <= 0:
        
        for i in range(1,n):
            
            if arr[i-1] + mid < arr[i] - mid:
                
                flag = 1
                
                break
            
        if flag == 1:
            
            lb = mid
            
        else:
            
            if arr[-1] + mid >= l:
                
                if round(ans, 10) == round(mid, 10):
                    
                    break
                
                ans = min(ans, mid)
                
                ub = mid
                
            else:
                
                lb = mid
        
    else:
        
        lb = mid
        
    if lb == prevlb and ub == prevub:
        
        break
        
    #print(lb,ub)
        
    #print(mid,ans)
        
print(round(ans, 10))

#print(round(499999999.99999994, 10))
