for _ in range(int(input())):
    
    word = input()
    
    codeforces,count = ['c', 'o', 'd', 'e', 'f', 'o', 'r', 'c', 'e', 's'],0
    
    for i,j in enumerate(word):
        
        if j != codeforces[i]:
            count += 1
            
    print(count)
