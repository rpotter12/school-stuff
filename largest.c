#include <stdio.h>
//#include <conio.h>

void main() {
    int x, y, z, largest;
    //clrscr();

    printf("Input 1st number: ");
    scanf("%d", &x);
    printf("Input 2nd number: ");
    scanf("%d", &y);
    printf("Input 3rd number: ");
    scanf("%d", &z);

    if (x > y && x > z) {
        largest = x;
    } else if (y > x && y > z) {
        largest = y;
    } else {
        largest = z;
    }

    printf("\nThe largest number is: %d", largest);
    //getch();
}
