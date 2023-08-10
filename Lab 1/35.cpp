#include <bits/stdc++.h>

using namespace std;

int main()
{
    double x_i = 50;

    for (int i = 0; i < 15; i++)
    {
        double f_x_i = x_i * x_i * x_i - x_i - 1;

        double d_f_x_i = 3 * x_i * x_i - 1;

        double x_i1 = x_i - f_x_i / d_f_x_i;

        double err = x_i1 - x_i;

        double re = err / x_i1;

        cout << std::fixed << std::setprecision(3);
        cout << "i = " << i << "\n";
        cout << "xi = " << x_i << "\n";
        cout << "f(xi) = " << f_x_i << "\n";
        cout << "f'(xi) = " << d_f_x_i << "\n";
        cout << "xi+1 = " << x_i1 << "\n";
        cout << "approx. error = " << err << "\n";
        cout << "rel. approx. error = " << re << "\n\n";

        x_i = x_i1;
    }
}