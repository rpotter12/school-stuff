#include <stdio.h>
//#include <conio.h>

void main() {
    long distance;
    //clrscr();

    printf("\nEnter value in Kilometers: ");
    scanf("%li", &distance);

    printf("\nValue in Meters     : %li", distance*1000);
    printf("\nValue in Centimeters: %li", distance*1000*100);
    printf("\nValue in Foot       : %li", distance*3280);
    printf("\nValue in Inches     : %li", distance*39370);

    //getch();
}
