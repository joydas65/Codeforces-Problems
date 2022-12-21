for _ in range(int(input())):
    
    n = int(input())
    
    word = input()
    
    freq,ans = [0 for i in range(26)],0
    
    for c in word:
        
        if freq[ord(c) - 65] == 0:
            
            ans += 2
            
        else:
            
            ans += 1
            
        freq[ord(c) - 65] += 1
            
    print(ans)
