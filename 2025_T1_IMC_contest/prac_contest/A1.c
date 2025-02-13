// only works for n<4000 not sure why array size of 4040 though

#include <stdio.h>

int ropes[4040];

int main(void) {
	int n, target;
	scanf("%d%d", &n, &target);

	int i, j;
	for (i = 0; i < n; i++)
		scanf("%d", &ropes[i]);

	for (i = 0; i < n; i++) {
		for (j = i + 1; j < n; j++) {
			if (ropes[i] + ropes[j] == target) {
				printf("YES\n%d %d\n", ropes[i], ropes[j]);
				return 0;
			}
		}
	}
	printf("NO\n");
	return 0;
}