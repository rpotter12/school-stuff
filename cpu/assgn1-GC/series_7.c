#include <stdio.h>

int main() {
    float factorial = 1;
    float sum = 0;

    for (int n=1; n<8; n++) {
        for (int i=2; i<=n; i++) {
            factorial *= i;
        }
        sum += (n/factorial);
    }

    printf("%f", sum);
}
