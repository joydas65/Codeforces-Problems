validCodes = dict()

validCodes["."] = 0
validCodes["-."] = 1
validCodes["--"] = 2

inp = input()

i,n,ans = 0,len(inp),""

while i+2 <= n or i+1 <= n:
	
	if i+2 <= n and inp[i:i+2] in validCodes:
		
		ans += str(validCodes[inp[i:i+2]])
		
		i += 2
		
	elif i+1 <= n and inp[i:i+1] in validCodes:
		
		ans += str(validCodes[inp[i:i+1]])
		
		i += 1
		
print(ans)
