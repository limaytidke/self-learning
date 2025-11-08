#include <stdio.h>

int main(void){
	int num,sum=0;
	printf("\nEnter number: ");
	scanf("%d",&num);
	while (num>0){
		sum+=num;
		num-=1;
	}
	printf("\nSUM: %d\n",sum);
}
