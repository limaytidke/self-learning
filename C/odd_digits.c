#include <stdio.h>

int main(void){
	int num,odd;
	printf("\nEnter number: ");
	scanf("%d",&num);
	for (num;num!=0;num/=10){
		odd = num%10;
		if (odd%2!=0){
			printf("%d ",odd);
		}
	}
}
