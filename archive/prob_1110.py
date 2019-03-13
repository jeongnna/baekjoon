n = int(input())
x = n
count = 0
while True:
    if x < 10:
        a, b = 0, x
    else:
        a, b = x // 10, x % 10
    x = 10 * b + (a + b) % 10
    count += 1
    if x == n:
        break
print(count)
