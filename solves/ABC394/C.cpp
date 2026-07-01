#include <iostream>
#include <string>
using namespace std;

int main()
{
    string S;
    cin >> S;

    int i = 0;
    while (i != S.length() - 1)
    {
        if (S.substr(i, 2) == "WA")
        {
            S.replace(i, 2, "AC");
            i--;
            if (i < 0)
            {
                i = 0;
            }
        }
        else
        {
            i++;
        }
    }

    cout << S << endl;
    return 0;
}
