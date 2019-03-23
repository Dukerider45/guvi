    
def longcomstr(l):
	ce=l[0]
	s=''
	n=len(ce)
	for i in range(1,len(l)):
		for j in range(0,len(l) and n):
			if ce[j]!=l[i][j]:
				break
			s=s+c[j]
	print(s)
def main():
	try:
		strarr=input()
		l=strarr.split()
		longcomstr(l)
	except:
		print('invalid')
    
main()
