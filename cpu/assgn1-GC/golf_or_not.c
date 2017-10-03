#include <stdio.h>

int main() {
    float temp;
    printf("Enter the temperature in fahrenheit: ");
    scanf("%f", &temp);

    if (temp >= 80) {
        printf("Go play golf");
    } else if (temp >=70 && temp < 80) {
        printf("Put on a jacket");
    } else {
        printf("It is way too cold.");
    }

    return 0;
}
