num = 2020

numbers = set()

for i in range(495):
    
    numbers.add(num * (i + 1))
    
num = 2021

for i in range(494):
    
    numbers.add(num * (i + 1))
    
s,upperBound = 0,10 ** 6

for i in range(496):
    
    for j in range(495):
        
        if ((2020 * i) + (2021 * j)) <= upperBound:
            numbers.add((2020 * i) + (2021 * j))
        else:
            break
        
for i in range(495):
    
    for j in range(496):
        
        if ((2021 * i) + (2020 * j)) <= upperBound:
            numbers.add((2021 * i) + (2020 * j))
        else:
            break

for _ in range(int(input())):
    
    n = int(input())
        
    print("YES" if n in numbers else "NO")
