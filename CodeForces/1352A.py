# Sum of Round Numbers

import sys

input = sys.stdin.read().strip().split('\n')

t = int(input[0])

integers = list(map(int, input[1:]))

for i in range(t):
    integer = integers[i]
    
    count = 10
    ans = []
    while integer > 0:
        remainder = integer % count
        if remainder != 0:
            ans.append(remainder)
            integer = integer - (remainder)
        count *= 10

    sys.stdout.write(f'{len(ans)}\n')
    sys.stdout.write(f' '.join(map(str, ans)) + '\n')

