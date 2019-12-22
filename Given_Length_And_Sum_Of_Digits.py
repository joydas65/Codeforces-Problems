def func(m,s):
    
    ans = ""
    
    while m >= 1:
        
        if s >= 10:
            
            ans += "9"
            
            s -= 9
            
        else:
            
            ans += str(s)
            
            s = 0
            
        m -= 1
        
    return ans
    
def compute(m,s):
    
    ans,c = "",0
    
    while m >= 1:
        
        digit = 0
        
        while 9*(m-1) < (s-digit):
            
            digit += 1
            
        if digit == 0 and c == 0:
            
            ans += "1"
            
            s -= 1
            
        else:
            
            ans += str(digit)
            
            s -= digit
        c += 1
        m -= 1
        
    return ans

m,s = map(int, input().split())

if m == 1 and s == 0:
    
    print("0 0")
    
elif m == 1 and s >= 10:
    
    print("-1 -1")
    
elif m == 1 and s >= 0 and s < 10:
    
    print(s,s)
    
elif m > 1 and s == 0:
    
    print("-1 -1")
    
elif 9*m < s:
    
    print("-1 -1")
    
else:
    
    v1 = compute(m,s)
    
    if len(str(v1)) == m:
        
        v2 = func(m,s)
        
        if len(str(v2)) == m:
            
            print(v1,v2)
            
        else:
            
            print("-1 -1")
            
    else:
        
        print("-1 -1")
