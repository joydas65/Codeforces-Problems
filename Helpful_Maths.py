s = input().split('+')

ones,twos,threes = 0,0,0

for i in s:
    
    if i == '1':
        
        ones += 1
        
    elif i == '2':
        
        twos += 1
        
    else:
        
        threes += 1
        
v = ones + twos + threes

if v >= 1 and ones >= 1:

    ch = '1'

for i in range(ones):
    
    if v > 1:
        
        print('1',end="+")
        
        v -= 1
        
if v >= 1 and twos >= 1:
        
    ch = '2'
        
for i in range(twos):
    
    if v > 1:
        
        print('2',end="+")
        
        v -= 1
        
if v >= 1 and threes >= 1:
        
    ch = '3'
        
for i in range(threes):
    
    if v > 1:
        
        print('3',end="+")
        
        v -= 1
        
print(ch)
