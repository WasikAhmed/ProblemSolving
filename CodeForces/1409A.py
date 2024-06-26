# Yet Another Two Integers Problem

import sys

input = sys.stdin.read().strip().split('\n')

integer = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
t = int(input[0].strip())
index = 1

for _ in range(t):
    arr = list(map(int, input[index].strip().split()))
    index += 1

    diff = abs(arr[0] - arr[1])
    ans = 0
    for i in integer:
        if diff >= i:
            ans += (diff // i)
            diff -= (diff // i) * i

    sys.stdout.write(f'{ans}\n')
