s = input()

n,f = len(s),0

for i in range(n):
    
    if s[i] == 'A':
        
        if i+1 < n and s[i+1] == 'B':
            f = 1
            break
        
if f == 1:
    x = i + 2
    
    for i in range(x,n):
        
        if s[i] == 'B':
            
            if i+1 < n and s[i+1] == 'A':
                
                f = 0
                break
    if f == 0:
        print("YES")
    else:
        f = 0
        for i in range(n):
            if s[i] == 'B':
                if i+1 < n and s[i+1] == 'A':
                    f = 1
                    break
        if f == 1:
            x = i + 2
            for i in range(x,n):
                if s[i] == 'A':
                    if i+1 < n and s[i+1] == 'B':
                        f = 0
                        break
            if f == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
                
else:
    print("NO")
