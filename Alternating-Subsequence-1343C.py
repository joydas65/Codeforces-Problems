for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    positiveNegativeSequenceLength, negativePositiveSequenceLength, c = 0,0,0
    
    for num in arr:
        
        if num > 0 and c % 2 == 0:
            
            positiveNegativeSequenceLength += 1
            c += 1
            
        elif num < 0 and c % 2 == 1:
            
            positiveNegativeSequenceLength += 1
            c += 1
            
    c = 0
            
    for num in arr:
        
        if num < 0 and c % 2 == 0:
            
            negativePositiveSequenceLength += 1
            c += 1
            
        elif num > 0 and c % 2 == 1:
            
            negativePositiveSequenceLength += 1
            c += 1
            
    if negativePositiveSequenceLength > positiveNegativeSequenceLength:
        
        ans,maxNegative,maxPositive,c = 0,-((10**9)+1),0,0
        
        for num in arr:
            
            if num > 0 and c % 2 == 0:
                c += 1
                ans += maxNegative
                maxNegative = -((10**9)+1)
            elif num < 0 and c % 2 == 1:
                c += 1
                ans += maxPositive
                maxPositive = 0
            
            if num < 0 and c % 2 == 0:
                maxNegative = max(maxNegative, num)
                
            elif num > 0 and c % 2 == 1:
                maxPositive = max(maxPositive, num)
                
        print(ans + maxNegative if c % 2 == 0 else ans + maxPositive)
        
    elif positiveNegativeSequenceLength > negativePositiveSequenceLength:
        
        ans,maxNegative,maxPositive,c = 0,-((10**9)+1),0,0
        
        for num in arr:
            
            if num > 0 and c % 2 == 1:
                c += 1
                ans += maxNegative
                maxNegative = -((10**9)+1)
            elif num < 0 and c % 2 == 0:
                c += 1
                ans += maxPositive
                maxPositive = 0
            
            if num < 0 and c % 2 == 1:
                maxNegative = max(maxNegative, num)
                
            elif num > 0 and c % 2 == 0:
                maxPositive = max(maxPositive, num)
                
        print(ans + maxNegative if c % 2 == 1 else ans + maxPositive)
