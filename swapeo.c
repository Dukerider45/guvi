
#include<stdio.h>
int main()
{
int n,i,count=0,j,k;
char a[100],th;
scanf("%[^\n]s",&a);
for(i=0;a[i]!='\0';i++)
{
count++;
}
for(i=0;i<count;i++)
{
if(i%2!=0)
{
th=a[i];
a[i]=a[i-1];
a[i-1]=th;
}
}
printf("%s",a);
return 0;
}
