#include <stdio.h>

int prime(int num){
	int i;
	if (num==1){
		return 3;
	}
	for (i=2;i<=num/2;i++){
		if (num%i==0){
			return 0;
		}
	}
	return 1;
}

int main(void){
	int num;
	printf("\nEnter number: ");
	scanf("%d",&num);
	if (prime(num)==1){
		printf("\nThe number is prime\n");
	}
	else if (prime(num)==3){
		printf("\nThe number is 1\n");
	}
	else{
		printf("\nThe number is not prime\n");
	}
}
