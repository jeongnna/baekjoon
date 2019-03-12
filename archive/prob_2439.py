n = int(input())
for i in range(n):
    n_stars = i + 1
    n_spaces = n - n_stars
    print(' ' * n_spaces + '*' * n_stars)
