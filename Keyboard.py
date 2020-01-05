s = input()

sentence = input()
ans = ""

for i in sentence:
    prev,flag = '',0
    for j in "qwertyuiopasdfghjkl;zxcvbnm,./":
        
        if flag == 1:
            break
        
        if i == j:
            
            if s == "R":
            
                break
            
            else:
                
                flag = 1
        
        prev = j
        
    if s == "R":
        
        ans += prev
        
    else:
        
        ans += j
    
print(ans)
