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

## 2. prob_2751 (시간초과)

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

None

## 5. prob_1427

None

## 6. prob_1181

None

