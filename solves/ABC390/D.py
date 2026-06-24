def dfs(idx, sz, n, a, s, val, st):
    for i in range(sz + 1):
        val ^= s[i]
        s[i] += a[idx]
        val ^= s[i]
        if idx == n - 1:
            st.add(val)
        elif i < sz:
            dfs(idx + 1, sz, n, a, s, val, st)
        else:
            dfs(idx + 1, sz + 1, n, a, s, val, st)
        val ^= s[i]
        s[i] -= a[idx]
        val ^= s[i]


n = int(input())
a = list(map(int, input().split()))
s = [0] * n
val = 0
st = set()
dfs(0, 0, n, a, s, val, st)
print(len(st))
