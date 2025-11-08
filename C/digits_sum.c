#include <stdio.h>

int main(void){
	int num,sum=0;
	printf("\nEnter number: ");
	scanf("%d",&num);
	for (num;num!=0;num/=10){
		sum = sum + num%10;
	}
	printf("\nsum: %d\n",sum);
}
