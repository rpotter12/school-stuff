#include <stdio.h>

int main() {
    int i, n, exp;
    float x;
    float sum = 1;
    float t = 1;

    printf("Enter the value for x : ");
    scanf("%f", &x);
    printf("\nEnter the value for n : ");
    scanf("%d", &n);

    for (i=1; i<=n; i++) {
        t = t*x/i;
        sum += t;
     }

    printf("%f", sum);
    return 0;
}
