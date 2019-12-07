s = input()

x,freq = set(),0

for i in s:
    
    if i not in x:
        
        freq += 1
        
        x.add(i)
        
if freq % 2 == 0:
    
    print("CHAT WITH HER!")
    
else:
    
    print("IGNORE HIM!")
