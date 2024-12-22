#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <strings.h>

#define MAX_NB_MONKEYS 2048
#define ITERS_PER_DAY  2000
#define NUMCHANGES     (ITERS_PER_DAY - 4)

int main(int argc, char *argv[])
{
	int secrets[MAX_NB_MONKEYS];
	int nb_monkeys = 0;
	FILE *f = fopen(argv[1], "r");
	char *line;
	ssize_t nread;
	size_t len;
	while ((nread = getline(&line, &len, f)) != -1) {
		long l = strtol(line, NULL, 10);
		assert(l <= INT_MAX);
		secrets[nb_monkeys++] = (int)l;
		printf("%ld\n", l);
	}
	fclose(f);
	printf("\n");
	long long total = 0;
	char *prices [MAX_NB_MONKEYS];
	char *changes[MAX_NB_MONKEYS];
	for (int i = 0; i < nb_monkeys; ++i) {
		prices[i] = malloc(sizeof(char) * ITERS_PER_DAY);
		changes[i] = malloc(sizeof(char) * 4 * NUMCHANGES);
	}
	char bestchanges[18][18][18][18];
	bzero(bestchanges, sizeof(bestchanges));
	for (int i = 0; i < nb_monkeys; ++i) {
		char min4 = -1;
		char min3 = -1;
		char min2 = -1;
		char min1 = -1;
		for (int x = 0; x < ITERS_PER_DAY; ++x) {
			int s = secrets[i];
			s ^= (s % 262144) << 6;
			s ^= s >> 5;
			s ^= (s % 8192) << 11;
			secrets[i] = s;
			char price = (char)(s % 10);
			prices[i][x] = price;
			if (min4 != -1) {
				char sub1 = min3  - min4;
				char sub2 = min2  - min3;
				char sub3 = min1  - min2;
				char sub4 = price - min1;
				changes[i][4 * (x-4) + 0] = sub1;
				changes[i][4 * (x-4) + 1] = sub2;
				changes[i][4 * (x-4) + 2] = sub3;
				changes[i][4 * (x-4) + 3] = sub4;
				if (price == 9)
					bestchanges[sub1+9][sub2+9][sub3+9][sub4+9] = 1;
			}
			min4 = min3;
			min3 = min2;
			min2 = min1;
			min1 = price;
		}
		printf("%d s=%d\n", i, secrets[i]);
		total += secrets[i];
	}
	printf("total: %lld\n", total);
	printf("sizeof(bestchanges)=%zu\n", sizeof(bestchanges));
	int bestchanges_nb = 0;
	for (int i = 0; i < 18; ++i)
	for (int j = 0; j < 18; ++j)
	for (int k = 0; k < 18; ++k)
	for (int l = 0; l < 18; ++l)
		if (bestchanges[i][j][k][l])
			++bestchanges_nb;
	printf("bestchanges_nb=%d\n", bestchanges_nb);
	int bestchanges_done = 0;
	int bestchange_total = 0;
	char bestchange[4] = {0};
	for (int i = 0; i < 18; ++i)
	for (int j = 0; j < 18; ++j)
	for (int k = 0; k < 18; ++k)
	for (int l = 0; l < 18; ++l) {
		if (!bestchanges[i][j][k][l])
			continue;
		total = 0;
		for (int m = 0; m < nb_monkeys; ++m) {
			for (int x = 0; x < NUMCHANGES; ++x) {
				if (changes[m][4*x + 0] == i - 9
				 && changes[m][4*x + 1] == j - 9
				 && changes[m][4*x + 2] == k - 9
				 && changes[m][4*x + 3] == l - 9) {
					total += prices[m][x+4];
					break;
				}
			}
		}
		if (bestchange_total < total) {
			bestchange_total = total;
			bestchange[0] = i-9;
			bestchange[1] = j-9;
			bestchange[2] = k-9;
			bestchange[3] = l-9;
		}
		printf("%.2f%%\r", 100.0 * bestchanges_done / bestchanges_nb);
		++bestchanges_done;
	}
	printf("bestchange_total=%d\n", bestchange_total);
	printf("bestchange = (%d, %d, %d, %d)\n",
		bestchange[0],
		bestchange[1],
		bestchange[2],
		bestchange[3]);
	for (int i = 0; i < nb_monkeys; ++i) {
		free(prices[i]);
		free(changes[i]);
	}
	return 0;
}
