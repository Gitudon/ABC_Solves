from collections import Counter

N = int(input())
A = list(map(int, input().split()))

count = Counter(A)
total_pairs = N * (N - 1) // 2
same_pairs = sum(v * (v - 1) // 2 for v in count.values())
ans = total_pairs - same_pairs
print(ans)
