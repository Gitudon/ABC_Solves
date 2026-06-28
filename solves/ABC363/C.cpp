#include <iostream>
#include <algorithm>
#include <string>
#include <set>
using namespace std;

int count_permutations_without_k_palindrome(int N, string S, int K)
{
    set<string> unique_permutations;
    sort(S.begin(), S.end());
    do
    {
        unique_permutations.insert(S);
    } while (next_permutation(S.begin(), S.end()));

    int ans = 0;
    for (const string &per : unique_permutations)
    {
        bool has_k_palindrome = false;
        for (int i = 0; i <= N - K; i++)
        {
            string substring = per.substr(i, K);
            string reversed_substring = substring;
            reverse(reversed_substring.begin(), reversed_substring.end());
            if (substring == reversed_substring)
            {
                has_k_palindrome = true;
                break;
            }
        }
        if (!has_k_palindrome)
        {
            ans++;
        }
    }
    return ans;
}

int main()
{
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;
    int result = count_permutations_without_k_palindrome(N, S, K);
    cout << result << endl;
    return 0;
}
