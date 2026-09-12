def manhattan_distance(x, y):
    return sum([abs(x[i] - y[i]) for i in range(len(x))])


def euclidean_distance(x, y):
    return sum([(x[i] - y[i]) ** 2 for i in range(len(x))]) ** 0.5


def chebyshev_distance(x, y):
    return max([abs(x[i] - y[i]) for i in range(len(x))])


N = int(input())
X = list(map(int, input().split()))

print(manhattan_distance([0] * N, X))
print(euclidean_distance([0] * N, X))
print(chebyshev_distance([0] * N, X))
