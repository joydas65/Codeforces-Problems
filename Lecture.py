n,m = map(int, input().split())

d1,d2 = dict(),dict()

for i in range(m):
    
    w1,w2 = map(str, input().split())
    
    d1[w1],d2[w2] = w2,w1
    
arr = list(map(str, input().split()))

for i in arr:
    
    if i in d1:
        
        n1,n2 = len(i),len(d1[i])
        
        if n1 == n2:
            
            print(i,end = " ")
            
        elif n1 > n2:
            
            print(d1[i],end = " ")
            
        else:
            
            print(i,end = " ")
            
    elif i in d2:
        
        n1,n2 = len(i),len(d2[i])
        
        if n1 == n2:
            
            print(d2[i],end = " ")
            
        elif n1 < n2:
            
            print(i,end = " ")
            
        elif n1 > n2:
            
            print(d2[i],end = " ")
