#Link to the question
#https://codeforces.com/problemset/problem/1409/A

for _ in range(int(input())):
    
    a,b = map(int, input().split())
    
    if a == b:
        
        print(0)
        
    else:
        
        x = abs(a-b)//10
        
        if abs(a-b) % 10 == 0:
            
            print(x)
            
        else:
            
            print(x+1)
