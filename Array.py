n = int(input())

arr = list(map(int, input().split()))

neg,a2 = [],""

for item in arr:
    
    if item < 0:
        
        neg.append(item)
        
    elif item > 0:
        
        a2 = a2 + str(item) + " "
        
a3,v = "",len(neg)
        
if v % 2 == 0:
    
    print(1,neg[0])
    
    a3 = "2 0 " + str(neg[1])
    
    for i in range(2,v):
        
        a2 = a2 + str(neg[i]) + " "
        
    print(n-3,a2)
    
    print(a3)
        
else:
    
    print(1,neg[0])
    
    for i in range(1,v):
        
        a2 = a2 + str(neg[i]) + " "
        
    print(n-2,a2)
    
    print(1,0)
