for _ in range(int(input())):
 
	n = int(input())
 
	if n % 3 == 0:
 
		print(n // 3, n // 3)
 
	elif n % 3 == 1:
 
		c1 = (n + 2) // 3
 
		print(c1,c1-1)
 
	else:
 
		c1 = (n - 2) // 3
 
		print(c1,c1+1)
