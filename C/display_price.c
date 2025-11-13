#include <stdio.h>

int main(void){
	float rice,sugar;
	printf("\nEnter price of rice: ");
	scanf("%f",&rice);
	printf("\nEnter price of sugar: ");
	scanf("%f",&sugar);
	printf("\n***LIST OF ITEMS***\n\nItem		Price\nRice		Rs %.2f\nSugar		Rs %.2f\n",rice,sugar);
}
