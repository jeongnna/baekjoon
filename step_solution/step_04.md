## 1. prob_9498

```python
score = int(input())
quo = score // 10
if quo >= 9:
    print('A')
elif quo == 8:
    print('B')
elif quo == 7:
    print('C')
elif quo == 6:
    print('D')
else:
    print('F')
```

## 2. prob_10817

```python
a, b, c = map(int, input().split())
if (b <= a and a <= c) or (c <= a and a <= b):
    print(a)
elif (a <= b and b <= c) or (c <= b and b <= a):
    print(b)
elif (a <= c and c <= b) or (b <= c and c <= a):
    print(c)
```

## 3. prob_10871

```python
_, x = map(int, input().split())
a = list(map(int, input().split()))
less_than_x = [str(v) for v in a if v < x]
print(' '.join(less_than_x))
```

## 4. prob_1546

```python
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
```

## 5. prob_4344

```python
n_cases = int(input())
for i in range(n_cases):
    input_list = list(map(int, input().split()))
    n = input_list[0]
    scores = input_list[1:]
    avg = 0
    for sc in scores:
        avg += sc
    avg /= n
    count = 0
    for sc in scores:
        if sc > avg:
            count += 1
    res = round(count / n * 100, 3)
    print('%.3f%%' % res)
```

## 6. prob_1110

```python
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
```

