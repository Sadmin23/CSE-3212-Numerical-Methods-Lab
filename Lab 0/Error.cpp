#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);

    double pre_apprx;

    cin >> pre_apprx;

    for (int i = 0; i < 4; i++)
    {
        double cur_apprx;
        cin >> cur_apprx;

        double apprx_error = cur_apprx - pre_apprx;

        pre_apprx = cur_apprx;

        double rel_apprx_error = (apprx_error / pre_apprx) * 100;

        cout << "Approxiamte Error= " << apprx_error << 
        "\nRelative Approximate Error= " << rel_apprx_error << "\n\n";
    }
}