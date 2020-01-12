n,m,k = map(int, input().split())

arr = []

for i in range(m+1):
    arr.append(int(input()))
    
v,y = "",arr[-1]

while y != 0:
    
    v += str(y % 2)
    
    y //= 2
    
h,v,ans = m-1,v[::-1],0

while h >= 0:
    
    f,t = arr[h],""
    
    while f != 0:
        
        t += str(f % 2)
        
        f //= 2
        
    n1,n2,t = len(t),len(v),t[::-1]
    
    if n1 > n2:
        
        v = "0"*(n1-n2) + v
        
    elif n1 < n2:
        
        t = "0"*(n2-n1) + t
        
    c = 0
        
    for i,j in enumerate(v):
        
        if j != t[i]:
            
            c += 1
            
    if c <= k:
        
        ans += 1
        
    h -= 1
print(ans)
