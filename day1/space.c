#include<stdio.h>
union abc{
	int a;
	float b;
	char c;
	double t;
}s1;
void main()
{
	printf("%d",sizeof(s1));
}
