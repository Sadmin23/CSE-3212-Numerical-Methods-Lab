#include <bits/stdc++.h>

using namespace std;

double f(double x)
{
    return x * x * x - x - 1;
}
void secant_method()
{
    double x_i0 = 50;
    double x_i1 = 48;

    for (int i = 0; i < 20; i++)
    {
        double f_x_i0 = f(x_i0);
        double f_x_i1 = f(x_i1);
        double d_f_x_i = (f_x_i1 - f_x_i0) / (x_i1 - x_i0);

        double x_i2 = x_i1 - f_x_i1 / d_f_x_i;
        double err = x_i2 - x_i1;
        double re = err / x_i2;

        cout << std::fixed << std::setprecision(6);
        cout << "i = " << i + 1 << "\n";
        cout << "xi-1 = " << x_i0 << ", f(xi-1) = " << f_x_i0 << "\n";
        cout << "xi = " << x_i1 << ", f(xi) = " << f_x_i1 << ", f'(xi) = " << d_f_x_i << "\n";
        cout << "xi+1 = " << x_i2 << "\n";
        cout << "approx. error = " << err << "\n";
        cout << "rel. approx. error = " << re << "\n\n";

        x_i0 = x_i1;
        x_i1 = x_i2;
    }
}
void newtons_raphson()
{
    double x_i = 50;

    for (int i = 0; i < 20; i++)
    {
        double f_x_i = x_i * x_i * x_i - x_i - 1;

        double d_f_x_i = 3 * x_i * x_i - 1;

        double x_i1 = x_i - f_x_i / d_f_x_i;

        double err = x_i1 - x_i;

        double re = err / x_i1;

        cout << std::fixed << std::setprecision(6);
        cout << "i = " << i + 1 << "\n";
        cout << "xi = " << x_i << "\n";
        cout << "f(xi) = " << f_x_i << "\n";
        cout << "f'(xi) = " << d_f_x_i << "\n";
        cout << "xi+1 = " << x_i1 << "\n";
        cout << "approx. error = " << err << "\n";
        cout << "rel. approx. error = " << re << "\n\n";

        x_i = x_i1;
    }
}
int main()
{
    secant_method();

//    newtons_raphson();

    return 0;
}