#include <stdio.h>
#include <stdlib.h> 

void fib(int n)
{

	int a = 0, b = 1, c, i;

	if (n <= 1)
		printf("%d ", a);
	else {

		printf("%d %d ", a, b);

		for (i = 3; i <= n; i++) {
			c = a + b;
			a = b;
			b = c;

			printf("%d ", c);
		}

		
	}
}

int main(int argc, char* argv[])
{

	int num, res = 0;
	if (argc == 1)
		printf("No command line arguments found.\n");

	else {
		num = atoi(argv[1]);
		fib(num);
	}
	return 0;
}
