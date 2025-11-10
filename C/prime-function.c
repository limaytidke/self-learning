//takes a number and checkes if its prime

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
