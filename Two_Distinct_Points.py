i = 0

for _ in range(int(input())):
    
    l1,r1,l2,r2 = map(int, input().split())
    
    x = set()
    x.add(l1)
    x.add(l2)
    x.add(r1)
    x.add(r2)
    
    if len(x) == 4:
        print(l1,l2)
        
    elif len(x) == 3:
        
        if l1 == l2:
            print(r1,r2)
        elif l1 == r1 or l2 == r2 or r1 == r2 or l1 == r2 or l2 == r1:
            print(l1,l2)
            
    elif len(x) == 2:
        
        if l1 == l2 and r2 == r1:
            
            print(l1,r1)
            
        elif l1 == r1 and l2 == r2:
            
            print(l1,l2)
            
        elif l1 == r2 and l2 == r1:
            
            print(l1,l2)
