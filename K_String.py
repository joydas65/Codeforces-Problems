n = int(input())

s = input()

d,f = dict(),0

for item in s:
    
    if item in d:
        
        d[item] += 1
        
    else:
        
        d[item] = 1
        
ans = ""
        
for item in d:
    
    if d[item] % n != 0:
        
        print(-1)
        
        f = 1
        
        break
    
    ans += (item*(d[item]//n))
    
if f == 0:
    
    print(ans*n)
