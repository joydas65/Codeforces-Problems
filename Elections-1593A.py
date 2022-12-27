for _ in range(int(input())):
    
    a,b,c = map(int, input().split())
    
    A = str(max((max(b,c) - a) + 1, 0))
    
    B = str(max((max(a,c) - b) + 1, 0))
    
    C = str(max((max(b,a) - c) + 1, 0))
    
    print(A+" "+B+" "+C)
