# Plus or Minus

import sys

input = sys.stdin.read().strip().split('\n')

t = int(input[0].strip())
index = 1

for _ in range(t):
    a, b, c = map(int, input[index].strip().split())
    index += 1

    if a + b == c:
        sys.stdout.write('+\n')
    else:
        sys.stdout.write('-\n')
