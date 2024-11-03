def check_even():
    rem = n - 2*k
    
    if rem < 0 or rem % 2 == 1:
        return False
        
    print("YES")
    
    for i in range(k-1):
        print(2,end=" ")
    print(2+n-2*k)
    
    return True
    
def check_odd():
    rem = n-k
    
    if rem < 0 or rem % 2 == 1:
        return False
        
    print("YES")
    
    for i in range(k-1):
        print(1,end=" ")
    print(1+n-k)
    
    return True

for _ in range(int(input())):
    
    n,k = map(int, input().split())
    
    if not (check_odd() or check_even()):
        print("NO")
    
