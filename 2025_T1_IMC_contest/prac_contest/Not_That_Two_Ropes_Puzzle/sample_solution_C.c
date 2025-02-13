// brute force solution for the problem

// tried to wrtie some test cases for this problem
// but it seems either I am not caplable of doing that or the problem is not suitable for that
// NOTE: 
//      - Memory usage here is fixed to 5000 * 4 bytes = 20KB
//      - Time measurement is also not usfull here as the time complexity is O(n^2), 
//        and it is very esay to tell if time out as the time limit is 1 second

#include <stdio.h>

int ropes[5000];

int main(void) {
    int n, target;
    scanf("%d %d", &n, &target);

    int i, j;
    for (i = 0; i < n; i++) {
        scanf("%d", &ropes[i]);
    }

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