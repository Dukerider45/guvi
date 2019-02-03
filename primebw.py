a,b= map(int,input().split())
for n in range(a+1,b+1):
	f=0
	for i in range(2,n//1):
			if n%i==0:
				f=1
				break
	if f==0:
		print(n)
