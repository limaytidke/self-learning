#include <stdio.h>

int main(void){
	int num,fact=1;
	printf("\nEnter number: ");
	scanf("%d",&num);
	if (num<0){
		printf("The factorial of a negative number doesn't exist");
	}
	else if (num == 0){
		printf("The factorial of 0 is 1");
	}
	else{
		for (num;num>0;num--){
			fact*=num;
		}
		printf("\nThe factorial is: %d\n",fact);
	}
}
