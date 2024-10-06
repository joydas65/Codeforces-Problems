for _ in range(int(input())):
    
    n = int(input())
    
    arr = []
    
    for i in range(n):
        arr.append(input())
        
    for i in range(n-1,-1,-1):
        for k,j in enumerate(arr[i]):
            if j == '#':
                print(k+1,end=" ")
    print()
