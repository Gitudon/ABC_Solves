n, m = map(int, input().split())

chosin_per_minute = 360 / 12 / 60
tansin_per_minute = 360 / 60

chosin_degree = chosin_per_minute * (n * 60 + m)
tansin_degree = tansin_per_minute * m

sa = abs(chosin_degree - tansin_degree) % 360

if sa > 180:
    print(360 - sa)
else:
    print(sa)
