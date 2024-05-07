#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_CHAR 256 // Assuming ASCII characters

typedef struct 
{
    char character;
    int frequency;
} CharFrequency;

int compare(const void *a, const void *b) {
    CharFrequency *cfa = (CharFrequency *)a;
    CharFrequency *cfb = (CharFrequency *)b;

    // Sort by frequency in descending order
    if (cfa->frequency != cfb->frequency) {
        return cfb->frequency - cfa->frequency;
    } else {
        // If frequencies are equal, sort alphabetically
        return cfa->character - cfb->character;
    }
}

CharFrequency* countCharacterFrequency(const char *str, int *numChars) {
    // Dynamically allocate memory for frequency array
    int *freq = (int*)calloc(MAX_CHAR, sizeof(int));
    if (freq == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        *numChars = 0;
        return NULL;
    }

    // Count frequencies
    while (*str) {
        if (isalpha(*str)) { // Ignore non-alphabetic characters
            freq[(unsigned char)*str]++;
        }
        str++;
    }

    // Count number of non-zero frequencies
    int count = 0;
    for (int i = 0; i < MAX_CHAR; i++) {
        if (freq[i] != 0) {
            count++;
        }
    }

    // Create array of CharFrequency structs
    CharFrequency *charFreqArray = (CharFrequency *)malloc(count * sizeof(CharFrequency));
    if (charFreqArray == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        *numChars = 0;
        free(freq);
        return NULL;
    }

    // Populate CharFrequency array
    int index = 0;
    for (int i = 0; i < MAX_CHAR; i++) {
        if (freq[i] != 0) {
            charFreqArray[index].character = (char)i;
            charFreqArray[index].frequency = freq[i];
            index++;
        }
    }

    // Sort the array
    qsort(charFreqArray, count, sizeof(CharFrequency), compare);

    // Set number of characters with non-zero frequency
    *numChars = count;

    // Free dynamically allocated memory
    free(freq);

    return charFreqArray;
}

const char* openfile(char* fileName) {
    FILE* fptr;
    fptr = fopen(fileName, "r");

    if (fptr == NULL) {
        printf("The file is not opened. The program will "
               "now exit.");
        exit(0);
    }
    fseek(fptr, 0, SEEK_END);
    long fsize = ftell(fptr);
    fseek(fptr, 0, SEEK_SET);  

    char *string = malloc(fsize + 1);
    fread(string, fsize, 1, fptr);
    fclose(fptr);

    for(int i = 0; string[i]; i++){
        string[i] = tolower(string[i]);
    }

    return string;
}

int binary(int n) {
    int i = 0;
    int binaryNum[32];
    int result = 0;

    // Convert decimal to binary
    while (n > 0) {
        binaryNum[i] = n % 2;
        n = n / 2;
        i++;
    }

    // Calculate binary number from array
    for (int j = i - 1; j >= 0; j--) {
        result = result * 10 + binaryNum[j];
    }

    return result;
}

int main() {
    char fileName[60];
    printf("Enter file name: \n");

    scanf("%s", fileName);
    printf("fileName is %s\n", fileName);

    const char *str = openfile(fileName);

    int numChars;
    CharFrequency *charFreqArray = countCharacterFrequency(str, &numChars);
    if (charFreqArray == NULL) {
        return 1; // Error handling
    }

    printf("Character frequencies (sorted):\n");
    for (int i = 0; i < numChars; i++) {
        printf("%c: %d: %d\n", charFreqArray[i].character, charFreqArray[i].frequency, binary(i));
    }

    // Free dynamically allocated memory
    free(charFreqArray);

    return 0;
}