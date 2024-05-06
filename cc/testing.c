
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#define MAX_CHAR 256 // Assuming ASCII characters


int main() {
    int n = 16;

    int i = 0;

    while (n > 0) {
        binary[i] = n % 2;
        n = n / 2;
        i++; 
    }

    for (int j = i - 1; j >= 0; j--)
        printf("%d", binary[j]);

    return 0;
}