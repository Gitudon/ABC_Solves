N = int(input())
a = list(map(int, input().split()))

jisho = {}
for i in range(N):
    jisho[a[i]] = i + 1

a.sort(reverse=True)
for sincho in a:
    print(jisho[sincho])
