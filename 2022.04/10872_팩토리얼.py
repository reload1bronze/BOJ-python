import sys

input = sys.stdin.readline

N = int(input())


def recursion(num):
    if num == 1 or num == 0:
        return 1
    return num * recursion(num - 1)


print(recursion(N))
