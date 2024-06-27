# Choosing Teams

import sys

input = sys.stdin.read().strip().split('\n')

t, k = map(int, input[0].strip().split())
participation = list(map(int, input[1].strip().split()))

# eligible = 0
# for x in participation:
#     if 5 - x >= k:
#         eligible += 1

eligible = len([x for x in participation if 5 - x >= k])

sys.stdout.write(f'{eligible // 3}\n')
