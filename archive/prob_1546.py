n = int(input())
scores = list(map(int, input().split()))
max_score = 0
for sc in scores:
    if sc > max_score:
        max_score = sc
avg = 0
for sc in scores:
    avg += sc / max_score * 100 / n
print(avg)
