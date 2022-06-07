for _ in range(int(input())):
    
    n = int(input())
    
    word = input()
    
    arr,i = [-1 for i in range(26)],0
    
    while i < n:
        
        if arr[ord(word[i]) - 65] != -1 and (i-1) >= 0 and word[i] != word[i-1]:
            
            print("NO")
            
            break
            
        arr[ord(word[i]) - 65] = i
        
        i += 1
        
    if i >= n:
        
        print("YES")
