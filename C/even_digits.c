#include <stdio.h>

int main(void){
	int num,even;
	printf("\nEnter number: ");
	scanf("%d",&num);
	for (num;num!=0;num/=10){
		even = num%10;
		if (even%2==0){
			printf("%d ",even);
		}
	}
}
