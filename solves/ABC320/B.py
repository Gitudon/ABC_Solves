S = input()


def expand(s, low, high, palindromes):
    while low >= 0 and high < len(s) and s[low] == s[high]:
        palindromes.add(s[low : high + 1])
        low = low - 1
        high = high + 1


def find_palindromic_substrings(s):
    palindromes = set()
    for i in range(len(s)):
        expand(s, i, i, palindromes)
        expand(s, i, i + 1, palindromes)
    ans = 0
    for u in palindromes:
        if len(u) > ans:
            ans = len(u)
    print(ans)


if __name__ == "__main__":
    find_palindromic_substrings(S)
