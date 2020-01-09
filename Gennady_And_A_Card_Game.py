s = input()

arr = list(map(str, input().split()))

flag = 0

for i in arr:
    
    if s[0] == i[0] or s[1] == i[1]:
        
        flag = 1
        break
if flag == 1:
    print("YES")
else:
    print("NO")
