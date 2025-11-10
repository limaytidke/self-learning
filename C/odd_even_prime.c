#include <stdio.h>
#include "prime-function.c"

int main(void){
	int num,odd=0,even=0,prime_counter=0;
	printf("\nEnter number: ");
	scanf("%d",&num);
	for (int i=1;i<=num;i++){
		if (i%2==0){
			even+=1;
		}
		else if (i%2!=0){
			odd+=1;
		}
		if (prime(i)==1){
			prime_counter+=1;
		}
	}
	printf("\nNumber of:\nEven no.= %d\nOdd no.= %d\nPrime no.= %d\n",even,odd,prime_counter);
}
