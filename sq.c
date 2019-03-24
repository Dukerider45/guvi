#include <stdio.h>

int main(void) {
	int n;
	int me,a,sum=0;
	scanf("%d",&n);
	while(n>0)
	{
		a=n%10;
		me=a*a;
		sum=sum+me;
		n=n/10;
	}
	printf("%d",sum);
	return 0;
}
