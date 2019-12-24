n = int(input())

arr = list(map(int, input().split()))

one,two,three,One,Two,Three = 0,0,0,[],[],[]

for i,j in enumerate(arr):
    
    if j == 1:
        
        one += 1
        One.append(i+1)
        
    elif j == 2:
        
        two += 1
        Two.append(i+1)
        
    elif j == 3:
        
        three += 1
        Three.append(i+1)
        
i1,i2,i3,ans,Ans = 0,0,0,0,[]

while one > 0 and two > 0 and three > 0:
    
    one -= 1
    two -= 1
    three -= 1
    
    ans += 1
    
    Ans.append((One[i1],Two[i2],Three[i3]))
    
    i1 += 1
    i2 += 1
    i3 += 1
    
if ans == 0:
    
    print(ans)
    
else:
    
    print(ans)
    
    for i in Ans:
        
        print(i[0],i[1],i[2])
