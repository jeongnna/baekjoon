_, x = map(int, input().split())
a = list(map(int, input().split()))
less_than_x = [str(v) for v in a if v < x]
print(' '.join(less_than_x))
