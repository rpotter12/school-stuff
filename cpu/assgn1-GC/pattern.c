#include <stdio.h>

int main() {
    int dots, init_spaces;

    for (int x=1; x<5; x++) {
        dots = x*2 - 1;
        init_spaces = (7-dots)/2;
        for (int i=0; i<init_spaces; i++) {
            printf(" ");
        }
        for (int j=0; j<dots; j++) {
            printf("*");
        }
        printf("\n");
    }

}
