from sortedcontainers import SortedList

event = []
st = SortedList()

N = int(input())
H = [0] * N
L = [0] * N
for i in range(N):
    H[i], L[i] = map(int, input().split())
    st.add(H[i])
    event.append((L[i] * 2, 0, i))

Q = int(input())
T = list(map(int, input().split()))

for i in range(Q):
    event.append((T[i] * 2 + 1, 1, i))

event.sort()

ans = [0] * Q
for tm, tp, i in event:
    if tp == 0:
        st.discard(H[i])
    else:
        ans[i] = st[-1]
for a in ans:
    print(a)
