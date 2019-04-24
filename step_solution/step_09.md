## 1. prob_2750

```python
def insert_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

n = int(input())
a = [int(input()) for i in range(n)]
insert_sort(a)
for i in range(n):
    print(a[i])
```

## 2. prob_2751

```python
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    if i1 < len(g1):
        a[ia:] = g1[i1:]
    if i2 < len(g2):
        a[ia:] = g2[i2:]

n = int(input())
a = [int(input()) for i in range(n)]
merge_sort(a)
for i in range(n):
    print(a[i])
```

## 3. prob_10989

None

## 4. prob_2108

```python
# https://3orento.tistory.com/73 를 참고하였음

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
```

## 5. prob_1427

```python
print(''.join(reversed(sorted(input()))))
```

## 6. prob_1181

None

