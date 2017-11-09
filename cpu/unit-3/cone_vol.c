#include <stdio.h>
#define PI 3.1415

int main() {
    int d, h;
    float vol;
    printf("Enter diameter of cone: ");
    scanf("%d", &d);
    printf("Enter height of cone: ");
    scanf("%d", &h);
    vol = PI*(d/2)*(d/2)*h*(1/3.0);
    printf("Volume of cone = %f", vol);
    return 0;
}
