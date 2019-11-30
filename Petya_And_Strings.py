s1 = input().lower()

s2 = input().lower()

#print(s1,s2)

n,flag = len(s1),0

for i in range(n):
    
    if s1[i] != s2[i]:
        
        if ord(s1[i]) < ord(s2[i]):
            
            print(-1)
            
        else:
            
            print(1)
            
        flag = 1
        
        break
    
if flag == 0:
    
    print(0)
