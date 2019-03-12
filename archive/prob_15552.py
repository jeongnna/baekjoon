import sys

T = int(input())
for t in range(T):
    string = sys.stdin.readline().rstrip()
    print(sum(map(int, string.split())))
