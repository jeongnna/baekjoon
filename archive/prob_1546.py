n = int(input())
scores = list(map(int, input().split()))
max_score = 0
for i in range(n):
    if scores[i] > max_score:
        max_score = scores[i]
avg = 0
for i in range(n):
    avg += scores[i] / max_score * 100 / n
print(avg)
