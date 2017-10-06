#include <stdio.h>

int main() {
    int sum = 0;
    int n = 105;
    while (n < 200) {
        sum += n;
        n += 5;
    }
    printf("%d", sum);
    return 0;
}
