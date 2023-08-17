#include <bits/stdc++.h>

using namespace std;

int iteration = 30;
const int n = 3;

double matrix[n][n] = {
    {4, -1, -1},
    {-2, 6, 1},
    {-1, 1, 7},
};

double result[n] = {3, 9, -6};

double x0[n] = {0, 0, 0};
double x1[n];

void linear_iteration()
{
    for (int k = 0; k < iteration; k++)
    {
        for (int i = 0; i < n; i++)
        {
            double sum = 0;

            for (int j = 0; j < n; j++)
            {
                if (i != j)
                    sum += matrix[i][j] * x0[j];
            }

            x1[i] = (result[i] - sum) / matrix[i][i];
        }

        for (int i = 0; i < n; i++)
        {
            x0[i] = x1[i];
        }

        printf("%f %f %f\n", x0[0], x0[1], x0[2]);
    }
}
int main()
{
    linear_iteration();

    return 0;
}