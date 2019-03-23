def main():
	f=1
	ne=int(input())
	for i in range(1,ne):
		f=f*i
	print(f)
try:
	main()
except:
	print('invalid')
