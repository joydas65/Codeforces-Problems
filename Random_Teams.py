n,m = map(int, input().split())

if m == 1:
    
    s = (n*(n-1))//2
    
    print(s,s)
    
else:

    last_team = n - m + 1
    
    s = (last_team * (last_team - 1))//2
    
    if s == 1:
        print("1 1")
    else:
        if n % m == 0:
            v = n//m
            x = (v*(v-1))//2
            print(x*m,s)
        else:
            v1,v2 = (n//m),(n//m)+1
            
            x = n%m
            y = (n - (x*v2))//v1
            s2,s1 = (v2*(v2-1))//2,(v1*(v1-1))//2
            print((x*s2)+(y*s1),s)
