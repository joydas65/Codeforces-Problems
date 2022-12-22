for _ in range(int(input())):

    keyboard = input()
    word = input()
    
    arr,ans = {},0
    
    for i,j in enumerate(keyboard):
        
        arr[j] = i
        
    for i,c in enumerate(word):
        
        if i >= 1:
        
            ans += abs(arr[c] - arr[word[i-1]])
        
    print(ans)
