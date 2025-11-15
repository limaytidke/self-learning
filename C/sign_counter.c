#include <stdio.h>

int main(void){
	int num,neg=0,pos=0;
	printf("\nEnter number: ");
	scanf("%d",&num);
	while (num!=0){
		if (num<0){
			neg+=1;
		printf("Enter number: ");
		scanf("%d",&num);
		}
		else{
			pos+=1;
		printf("Enter number: ");
		scanf("%d",&num);
		}
	}
	printf("\nNegative number count: %d\nPositive number count: %d",neg,pos);
}
