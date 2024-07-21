for _ in range(int(input())):
    
    s = input()
    
    d = {'A': 0, 'B': 0}
    
    for i in s:
        
        d[i] += 1
        
    print('A' if d['A'] > d['B'] else 'B')
