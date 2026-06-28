N = int(input())
A = list(map(int, input().split()))


class Ameba:
    def __init__(self, n, i):
        self.sedai = n
        self.number = i

    def return_sedai(self):
        return self.sedai


Ameba_list = [0] * (2 * N + 2)
Ameba_list[1] = Ameba(0, 1)
for i in range(1, N + 1):
    sedai = Ameba_list[A[i - 1]].return_sedai()
    Ameba_list[2 * i] = Ameba(sedai + 1, 2 * i)
    Ameba_list[2 * i + 1] = Ameba(sedai + 1, 2 * i + 2)

for i in range(1, 2 * N + 2):
    print(Ameba_list[i].return_sedai())
