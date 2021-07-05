try:
	for t in range(int(input())):
		d,x,y,z = map(int,input().strip().split())
		print(int(max((x*7),((y*d)+z*(7-d)))))

except:
	pass