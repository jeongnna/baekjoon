## 1. prob_2741

```python
n = int(input())
for i in range(n):
    print(i + 1)
```

## 2. prob_2742

```python
n = int(input())
for i in range(n, 0, -1):
    print(i)
```

## 3. prob_2739

```python
n = int(input())
for i in range(1, 10):
    print(str(n) + ' * ' + str(i) + ' = ' + str(n * i))
```

## 4. prob_2438

```python
n = int(input())
for i in range(n):
    print('*' * (i + 1))
```

## 5. prob_2439

```python
n = int(input())
for i in range(n):
    n_stars = i + 1
    n_spaces = n - n_stars
    print(' ' * n_spaces + '*' * n_stars)
```

## 6. prob_2440

```python
n = int(input())
for i in range(n, 0, -1):
    print('*' * i)
```

## 7. prob_2441

```python
n = int(input())
for i in range(n):
    n_spaces = i
    n_stars = n - i
    print(' ' * n_spaces + '*' * n_stars)
```

## 8. prob_1924

```python
def weekday(month, day):
    n_days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    weekdays = {
        0: 'SUN',
        1: 'MON',
        2: 'TUE',
        3: 'WED',
        4: 'THU',
        5: 'FRI',
        6: 'SAT'
    }
    day_of_year = 0
    for month in range(1, x):
        day_of_year += n_days_in_month[month]
    day_of_year += y
    return weekdays[day_of_year % 7]

x, y = map(int, input().split())
print(weekday(x, y))
```

## 9. prob_8393

```python
n = int(input())
res = 0
for i in range(n):
    res += i + 1
print(res)
```

## 10. prob_11720

```python
n = int(input())
nums = input()
res = 0
for i in range(n):
    res += int(nums[i])
print(res)
```

## 11. prob_11721

```python
string = input()
n_iters = 1 + len(string) // 10
for i in range(n_iters):
    print(string[(10 * i):(10 * (i + 1))])
```

## 12. prob_15552

```python
import sys

T = int(input())
for t in range(T):
    string = sys.stdin.readline().rstrip()
    print(sum(map(int, string.split())))
```

