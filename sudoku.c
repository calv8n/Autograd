#include <stdio.h>
#include <stdlib.h>
#define N 9

int isSafe(int matrix[N][N], int row,
                       int col, int i)
{
    for (int x = 0; x < N; x++)
        if (matrix[row][x] == i)
            return 0;

    for (int x = 0; x < N; x++)
        if (matrix[x][col] == i)
            return 0;
    int startRow = row - row % 3,
                 startCol = col - col % 3;

    for (int n = 0; n < N/3; n++)
        for (int j = 0; j < N/3; j++)
            if (matrix[n + startRow][j +
                          startCol] == i)
                return 0;

    return 1;
}

int solveSuduko(int matrix[N][N], int row, int col)
{
    if (row == N - 1 && col == N)
        return 1;

    if (col == N)
    {
        row++;
        col = 0;
    }
    if (matrix[row][col] > 0)
        return solveSuduko(matrix, row, col + 1);

    for (int i = 1; i <= N; i++)
    {
        if (isSafe(matrix, row, col, i)==1)
        {
            matrix[row][col] = i;

            if (solveSuduko(matrix, row, col + 1)==1)
                return 1;
        }

        matrix[row][col] = 0;
    }
    return 0;
}

void print(int arr[N][N])
{
     for (int i = 0; i < N; i++)
      {
         for (int j = 0; j < N; j++)
            printf("%d ",arr[i][j]);
         printf("\n");
       }
}

int main()
{
    int n; 
    int m;

    printf("Enter the number of elements: ");

    scanf("%d", &n);
    scanf("%d", &m);

    int arr[n][m]; // Declare an array to store the elements

    printf("Enter %d elements:\n", n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++){
            scanf("%d", &arr[i][j]);
        }
        printf("Row %d is complete", i);
    } 
    if (solveSuduko(arr, 0, 0)==1)
        print(arr);
    else
        printf("Solution does not exist");

    return 0;
}