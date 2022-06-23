for _ in range(int(input())):
    
    s = input()
    
    d = dict()
    d['A'] = 0
    d['B'] = 0
    d['C'] = 0
    
    for character in s:
        
        d[character] += 1
        
    if d['A'] + d['C'] == d['B']:
        
        print("YES")
        
    elif d['A'] == 0 and d['B'] == d['C']:
        
        print("YES")
        
    elif d['C'] == 0 and d['B'] == d['A']:
        
        print("YES")
        
    else:
        
        print("NO")
