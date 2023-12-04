#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <rows> <columns>\n", argv[0]);
        return 1;
    }

    int rows = atoi(argv[1]);
    int columns = atoi(argv[2]);

    if (argc != rows * columns + 3) {
        printf("Invalid number of elements provided. Expected %d elements.\n", rows * columns);
        return 1;
    }

    int matrix[rows][columns];

    // Convert command-line arguments to integers and store them in the matrix
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            matrix[i][j] = atoi(argv[i * columns + j + 3]);
        }
    }

    // Display the entered matrix
    printf("Entered matrix:\n");
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}
