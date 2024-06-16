# Lucky?

import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    ticket_digits = list(map(int, sys.stdin.readline().strip()))
    if sum(ticket_digits[:3]) == sum(ticket_digits[3:]):
        sys.stdout.write('YES\n')
    else:
        sys.stdout.write('NO\n')
