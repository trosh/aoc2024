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

long long check(long long result, int *operands, int nb_operands, int nb_operators)
{
	char cat[1024];
	int nb_combinations = powi(nb_operators, nb_operands - 1);
	//printf("nb_combinations = %d\n", nb_combinations);
	for (int c = 0; c < nb_combinations; ++c) {
		int cc = c;
		long long total = operands[0];
		for (int o = 1; o < nb_operands; ++o) {
			switch (cc % nb_operators) {
			case 0:
				total += operands[o];
				//printf("+");
				break;
			case 1:
				total *= operands[o];
				//printf("*");
				break;
			case 2:
				if (0) {
					snprintf(cat, 1024, "%lld%d", total, operands[o]);
					total = strtoll(cat, NULL, 10);
				} else {
					int pow10 = 1;
					while (pow10 <= operands[o])
						pow10 *= 10;
					total *= pow10;
					total += operands[o];
				}
				break;
			}
			cc /= nb_operators;
			//if (total > result)
			//	break;
		}
		if (total == result) {
			//printf("OK!\n");
			return result;
		}
		//printf("total=%lld\n", total);
	}
	return 0;
}

int main(void)
{
	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	long long sumres = 0;
	long long sumres2 = 0;
	while ((read = getline(&line, &len, stdin)) != -1) {
		char *str = strtok(line, ": ");
		long long result = strtoll(str, NULL, 10);
		//printf("%lld: ", result);
		int nb_operands = 0;
		int operands[1024];
		while ((str = strtok(NULL, " \n"))) {
			operands[nb_operands++] = atoi(str);
		}
		for (int o = 0; o < nb_operands; ++o) {
			//printf("%d ", operands[o]);
		}
		//printf("\n");
		sumres  += check(result, operands, nb_operands, 2);
		sumres2 += check(result, operands, nb_operands, 3);
	}
	printf("part1: %lld\n", sumres);
	printf("part2: %lld\n", sumres2);
	return EXIT_SUCCESS;
}
