for _ in range(int(input())):
    
    k = int(input())
    
    s = input()
    ans,flag,c = 0,0,0
    
    for i in s:
        
        if i == 'A':
            c = 0
            flag = 1
        elif i == 'P':
            if flag == 1:
                c += 1
                ans = max(ans, c)
    print(max(ans,c))
