n = int(input())
for i in range(n):
    n_spaces = i
    n_stars = n - i
    print(' ' * n_spaces + '*' * n_stars)
