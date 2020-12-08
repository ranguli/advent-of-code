#include <stdio.h>
#include <stdlib.h>

/**
 * Designed to be compiled in TurboC v1.0, and ran on my Tandy 1000 SL/2 with
 * an Intel 8086 and 640KB of RAM :)
 * */

int countlines(char filename[]) {
    FILE *fp;
    int lines;
    char ch;

    fp = fopen(filename, "r");
    lines = 0;

    while(!feof(fp))
    {
       ch = fgetc(fp);

       if (ch == '\n')
           lines++;
    }

    return lines;
}

main() {
    FILE *in_file;
    char line[100];
    char filename[] = "input.txt";
    int file_size;
    int i, j;
    unsigned int product;
    int remaining;
    int expenses[200];

    in_file = fopen(filename, "r");
    file_size = countlines(filename);

    if (in_file == NULL) {
        printf("Could not open file!");
        exit(-1);
    }

    for (i = 0; i <= file_size; i++) {
        fgets(line, 100, in_file);
        expenses[i] = atoi(line);
    }

    for (i = 0; i <= file_size; i++) {
        for (j = i; j < file_size; j++) {
            if (expenses[i] + expenses[j] == 2020) {
                product = expenses[i] * expenses[j];
                printf("%d x %d = %u\n", expenses[i], expenses[j], product);
                exit(0);
            }
        }
    }
}
