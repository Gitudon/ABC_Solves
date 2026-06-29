N = int(input())
A = list(map(int, input().split()))
ans = ["a"] * N
for i in range(3 * N):
    if ans[A[i] - 1] == "a":
        ans[A[i] - 1] = "b"
    elif ans[A[i] - 1] == "b":
        ans[A[i] - 1] = i
indexed_arr = [(i, x) for i, x in enumerate(ans)]
sorted_arr = sorted(indexed_arr, key=lambda x: x[1])
for i, x in sorted_arr:
    print(i + 1)
