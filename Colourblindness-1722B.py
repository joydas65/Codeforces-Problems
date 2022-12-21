for _ in range(int(input())):
    
    n = int(input())
    
    word1 = input()
    word2 = input()
    
    i = 0
    
    while i < n:
        
        c1,c2 = word1[i],word2[i]
        
        if (c1 == 'G' and c2 == 'B') or (c1 == 'B' and c2 == 'G') or (c1 == c2):
            i += 1
        else:
            break
        
    print("YES" if i == n else "NO")
