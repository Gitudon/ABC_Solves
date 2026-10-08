A, B, C = map(int, input().split())

a = [
    10 * A + B + C,
    10 * A + C + B,
    10 * B + A + C,
    10 * B + C + A,
    10 * C + A + B,
    10 * C + B + A,
]
print(max(a))
