try:
	for t in range(int(input())):
		n,k = map(int,input().strip().split())
		A = list(map(int,input().strip().split()))
		ans,p = 0,31

		while ((sum(A)!=0) and (p>=0)):
			count = 0
			for j in range(n):				
				if(A[j] >= (2 ** p)):
					A[j] -= (2**p)
					count +=1
			if ((count % k) == 0):
				ans += (count/k)
			else:
				ans += int(count/k)+1
			p -=1
		print(int(ans))

except:
	pass