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
