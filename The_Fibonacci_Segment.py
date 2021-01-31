# Question Link - https://codeforces.com/problemset/problem/365/B

n = int(input())

arr = list(map(int, input().split()))

i,ans,c = n-1,0,0

while i-2 >= 0:
    
    if arr[i] == arr[i-1] + arr[i-2]:
        
        c += 1
        
    else:
        
        if c > 0:
        
            ans = max(ans, c+2)
            
        else:
            
            ans = max(ans, 1)
        
        c = 0
        
    i -= 1
    
if c > 0:
    
    print(max(ans, c+2))
    
else:
    
    if ans == 1 and n > 1:
        
        print(2)
        
    elif n == 1 or n == 2:
        
        print(n)
        
    else:
        
        print(ans)
