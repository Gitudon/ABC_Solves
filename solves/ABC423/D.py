from collections import deque
from sortedcontainers import SortedList

N, K = map(int, input().split())
que = deque()
for i in range(N):
    a, b, c = map(int, input().split())
    que.append((a, b, c))

current_customers = 0
current_time = 0
next_taiten = (0, 0)
next_customer = (0, 0, 0)
taiten_machi = SortedList(key=lambda x: x[0])
while que:
    next_customer = que.popleft()
    while current_customers + next_customer[2] > K:
        if not taiten_machi:
            current_time = next_taiten[0]
            current_customers -= next_taiten[1]
            next_taiten = (0, 0)
        else:
            taiten = taiten_machi.pop(0)
            current_time = taiten[0]
            current_customers -= taiten[1]
            if taiten_machi:
                next_taiten = taiten_machi[0]
            else:
                next_taiten = (0, 0)
    if current_time < next_customer[0]:
        current_time = next_customer[0]
    print(current_time)
    current_customers += next_customer[2]
    taiten = (current_time + next_customer[1], next_customer[2])
    taiten_machi.add(taiten)
