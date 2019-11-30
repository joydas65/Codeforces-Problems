solved = 0

for _ in range(int(input())):
    
    a,b,c = map(int, input().split())
    
    if (a == 1 and b == 1) or (a == 1 and c == 1) or (b == 1 and c == 1) or (a == 1 and b == 1 and c == 1):
        
        solved += 1
        
print(solved)
