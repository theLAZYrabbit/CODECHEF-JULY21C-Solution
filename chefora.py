try:
	s, arr = 0, [0]

	#making an array of all chefora numbers
	for i in range(1,100001):
		#since all chefora numbers are palindromes like 13231, using slicing create those numbers
		s+= int(str(i)[:-1] +str(i)[::-1])
		arr.append(s)

	for q in range(int(input())):
		l,r = map(int,input().strip().split())
		
		#ans is the mod of l'th element power the sum of l+1 to the r'th element 
		ans = pow((arr[l] - arr[l-1]), (arr[r] - arr[l]), 1000000007)

		print(int(ans))
		print(arr[l])
		print(arr [l-1])

except:
	pass