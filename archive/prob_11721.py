string = input()
n_iters = 1 + len(string) // 10
for i in range(n_iters):
    print(string[(10 * i):(10 * (i + 1))])
