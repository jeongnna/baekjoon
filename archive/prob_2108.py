import sys
from collections import Counter


n = int(sys.stdin.readline())
a = [None] * n
for i in range(n):
    a[i] = int(sys.stdin.readline())
a.sort()

print(round(sum(a) / n))  # average

if n == 1:
    print(a[0])  # median
    print(a[0])  # mode
    print(0)     # range

else:
    print(a[n // 2])  # median
    
    # mode
    cnt = Counter(a)
    cnt = sorted(cnt.items(), key = lambda x: (-x[1], x[0]))
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
    
    print(a[-1] - a[0])  # range
