# Dislike of Threes

import sys

input = sys.stdin.read().strip().split('\n')

t = int(input[0])

integers = list(map(int, input[1:]))
ans = [1] * t

for i in range(t):
    count, current_integer = 1, 1

    while count <= integers[i]:
        if not ((current_integer % 3 == 0) or (current_integer % 10 == 3)):
            count += 1
            ans[i] = current_integer
        current_integer += 1

sys.stdout.write(f'\n'.join(map(str, ans)))
