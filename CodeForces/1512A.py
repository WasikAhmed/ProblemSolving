# Spy Detected!

import sys

input = sys.stdin.read().strip().split('\n')

t = int(input[0].strip())
index = 1

for _ in range(t):
    n = int(input[index].strip())
    index += 1
    arr = list(map(int, input[index].strip().split()))
    index += 1

    s = set(arr)
    a, b = iter(s)

    if arr.count(a) < arr.count(b):
        sys.stdout.write(f'{arr.index(a) + 1}\n')
    else:
        sys.stdout.write(f'{arr.index(b) + 1}\n')
