for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    one_to_n = [0 for i in range(n+1)]
    
    for item in arr:
        
        if one_to_n[item] == 0:
            
            one_to_n[item] = -1
            
            print(item, end = " ")
            
    print()
