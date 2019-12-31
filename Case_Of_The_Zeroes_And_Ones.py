n = int(input())

s = input()

arr,c = [],0

for i in s:
    
    if c > 0 and arr[-1] == '0' and i == '1':
        
        arr.pop()
        c -= 1
        
    elif c > 0 and arr[-1] == '1' and i == '0':
        
        arr.pop()
        c -= 1
        
    else:
        arr.append(i)
        c += 1
        
print(len(arr))
