n,m = map(int, input().split())

v = m

while 2*v < n:
    
    v += m
    
two,one,flag = v,0,0
    
while two >= 0 and one <= v:
    
    if (two*2) + (one*1) == n:
        
        print(v)
        flag = 1
        break
    
    two -= 1
    one += 1
if flag == 0:
    print(-1)
