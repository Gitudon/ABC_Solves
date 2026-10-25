Q = int(input())

accounts = {}
current_id = 1
for _ in range(Q):
    s = input()
    if s not in accounts:
        accounts[s] = current_id
        current_id += 1
    print(accounts[s])
