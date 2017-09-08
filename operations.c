#include <stdio.h>
//#include <conio.h>

void main() {
    long m, n;
    //clrscr();

    printf("Enter 1st number: ");
    scanf("%li", &m);

    printf("Enter 2nd number: ");
    scanf("%li", &n);

    printf("\nAdding      : %li", n+m);
    printf("\nSubtracting : %li", n-m);
    printf("\nMultiplying : %li", n*m);
    printf("\nDividing    : %li", n/m);
    printf("\nModulus     : %li", n%m);

    //getch();
}
