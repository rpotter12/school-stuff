#include <stdio.h>
//#include <conio.h>

void main() {
    int a, b, y, z;
    //clrscr();

    printf("Prefix in C:\n");

    a = 5;
    printf("\nInitial value of a: %d\n", a);

    printf("\nAssigning b = ++a\n");
    b = ++a;

    printf("Value of a: %d\n", a);
    printf("Value of b: %d\n", b);

    printf("\nAssigning b = --a\n");
    b = --a;

    printf("Value of a: %d\n", a);
    printf("Value of b: %d\n", b);

    printf("\n\nPostfix in C:");

    y = 5;
    printf("\n\nInitial value of y: %d\n", y);

    printf("\nAssigning z = y++\n");
    z = y++;

    printf("Value of y: %d\n", y);
    printf("Value of z: %d\n", z);

    printf("\nAssigning z = y--\n");
    z = y--;

    printf("Value of y: %d\n", y);
    printf("Value of z: %d\n", z);

    //getch();
}
