for _ in range(int(input())):
    
    s1 = input()
    s2 = input()
    
    i,n = 0,len(s1)
    
    while i < n:
        
        if s2[0] == s1[i]:
            break
        
        i += 2
        
    print("YES" if i < n else "NO")
