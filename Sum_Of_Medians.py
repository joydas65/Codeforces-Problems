def compute(ar, N, K, V):
    
    c,ans,i = 0,0,N*K
    
    while c != K:
        
        ans += ar[i - V]
        
        i -= V
        
        c += 1
        
    return ans

for _ in range(int(input())):
    
    n,k = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    v = (n//2)+1
    
    print(compute(arr,n,k,v))
