import queue

Q = int(input())
q = queue.Queue()
height = [0] * (Q + 1)
for i in range(Q):
    query = input().split()
    if query[0] == "1":
        height[i + 1] = height[i]
        q.put(i)
    elif query[0] == "2":
        height[i + 1] = height[i] + int(query[1])
    else:
        height[i + 1] = height[i]
        ans = 0
        h = int(query[1])
        while not q.empty():
            if height[i + 1] - height[q.queue[0]] >= h:
                ans += 1
                q.get()
            else:
                break
        print(ans)
