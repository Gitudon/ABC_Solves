import queue

mod = 10**9
N, K = map(int, input().split())
q = queue.Queue()
for _ in range(K):
    q.put(1)
current_sum = K
end = 1

for _ in range(N + 1 - K):
    q.put(current_sum)
    end = current_sum
    current_sum += end - q.get()
    current_sum %= mod

print(end % mod)
