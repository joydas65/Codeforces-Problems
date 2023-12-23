for _ in range(int(input())):
    
    n = int(input())
    
    nums = list(map(int, input().split()))
    
    small,ind,prod = 10 ** 8,-1,1
    
    for i,j in enumerate(nums):
        
        if j < small:
            
            small,ind = j,i
            
    for i,j in enumerate(nums):
        
        if i == ind:
            
            prod *= (small + 1)
            
        else:
            
            prod *= j
            
    print(prod)
