n = int(input())

n1 = input()
n2 = input()

i,ans = 0,0

while i < n:
    
    a,b = ord(n1[i])-48,ord(n2[i])-48
    
    if a > b:
        
        ans += min(10 - a + b, abs(a-b))
        
    elif a < b:
        
        ans += min(a + 10 - b, abs(a-b))
    
    i += 1

print(ans)
