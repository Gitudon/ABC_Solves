N, M = map(int, input().split())

friends = [set() for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    friends[A - 1].add(B - 1)
    friends[B - 1].add(A - 1)

for i in range(N):
    friend_of_friends = set()
    for friend in friends[i]:
        friend_of_friends.update(friends[friend])
    # 自分自身と直接の友達は除外
    friend_of_friends.discard(i)
    friend_of_friends.difference_update(friends[i])
    print(len(friend_of_friends))
