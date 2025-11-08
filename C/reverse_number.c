#include <stdio.h>

int main(void){
	int num,reverse=0;
	printf("\nEnter number: ");
	scanf("%d",&num);
	for (num;num!=0;num/=10){
		reverse = reverse*10 + num%10;
	}
	printf("\nreversed: %d\n",reverse);
}
