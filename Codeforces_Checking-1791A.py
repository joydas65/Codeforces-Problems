chars = set()

chars.add("c")
chars.add("o")
chars.add("d")
chars.add("e")
chars.add("f")
chars.add("r")
chars.add("s")

for _ in range(int(input())):
    
    s = input()
    
    print('YES' if s in chars else "NO")
    
