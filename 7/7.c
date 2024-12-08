#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int powi(int n, int p)
{
	int r = 1;
	for (int i = 0; i < p; ++i)
		r *= n;
	return r;
}

int main(void)
{
	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	long long sumres = 0;
	while ((read = getline(&line, &len, stdin)) != -1) {
		char *str = strtok(line, ": ");
		printf("[%s] ", str);
		long long result = strtoll(str, NULL, 10);
		printf("%lld: ", result);
		int nb_operands = 0;
		int operands[1024];
		while ((str = strtok(NULL, " \n"))) {
			operands[nb_operands++] = atoi(str);
		}
		for (int o = 0; o < nb_operands; ++o) {
			//printf("%d ", operands[o]);
		}
		printf("\n");
		int nb_combinations = powi(2, nb_operands - 1);
		//printf("nb_combinations = %d\n", nb_combinations);
		for (int c = 0; c < nb_combinations; ++c) {
			int cc = c;
			long long total = operands[0];
			for (int o = 1; o < nb_operands; ++o) {
				if (cc % 2 == 0) {
					total += operands[o];
					printf("+");
				} else {
					total *= operands[o];
					printf("*");
				}
				cc /= 2;
			}
			if (total == result) {
				printf("OK!\n");
				sumres += (long long)result;
				break;
			}
			printf("total=%lld\n", total);
		}
	}
	printf("%lld\n", sumres);
	return EXIT_SUCCESS;
}
