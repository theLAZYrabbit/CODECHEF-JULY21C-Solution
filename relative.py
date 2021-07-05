try:
	for i in range(int(input())):
		g,c=map(int,input().strip().split())
		minh = (c**2) / (2 * g)
		print(int(minh))

except:
	pass