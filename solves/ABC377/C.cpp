#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main()
{
    long long N, M;
    cin >> N >> M;
    vector<int> a(M), b(M);
    for (int i = 0; i < M; ++i)
    {
        cin >> a[i] >> b[i];
        a[i]--; // Convert to 0-based index
        b[i]--;
    }
    set<pair<int, int>> field;
    long long ans = N * N;
    for (int i = 0; i < M; ++i)
    {
        field.insert({a[i], b[i]});
        ans--;
    }
    for (int i = 0; i < M; ++i)
    {
        if (a[i] + 2 < N)
        {
            if (b[i] + 1 < N && field.find({a[i] + 2, b[i] + 1}) == field.end())
            {
                field.insert({a[i] + 2, b[i] + 1});
                ans--;
            }
            if (b[i] - 1 >= 0 && field.find({a[i] + 2, b[i] - 1}) == field.end())
            {
                field.insert({a[i] + 2, b[i] - 1});
                ans--;
            }
        }
        if (a[i] - 2 >= 0)
        {
            if (b[i] + 1 < N && field.find({a[i] - 2, b[i] + 1}) == field.end())
            {
                field.insert({a[i] - 2, b[i] + 1});
                ans--;
            }
            if (b[i] - 1 >= 0 && field.find({a[i] - 2, b[i] - 1}) == field.end())
            {
                field.insert({a[i] - 2, b[i] - 1});
                ans--;
            }
        }
        if (b[i] + 2 < N)
        {
            if (a[i] + 1 < N && field.find({a[i] + 1, b[i] + 2}) == field.end())
            {
                field.insert({a[i] + 1, b[i] + 2});
                ans--;
            }
            if (a[i] - 1 >= 0 && field.find({a[i] - 1, b[i] + 2}) == field.end())
            {
                field.insert({a[i] - 1, b[i] + 2});
                ans--;
            }
        }
        if (b[i] - 2 >= 0)
        {
            if (a[i] + 1 < N && field.find({a[i] + 1, b[i] - 2}) == field.end())
            {
                field.insert({a[i] + 1, b[i] - 2});
                ans--;
            }
            if (a[i] - 1 >= 0 && field.find({a[i] - 1, b[i] - 2}) == field.end())
            {
                field.insert({a[i] - 1, b[i] - 2});
                ans--;
            }
        }
    }
    cout << ans << endl;
    return 0;
}
