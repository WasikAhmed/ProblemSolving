# Holiday Of Equality

import sys

n = int(sys.stdin.readline().strip())
welfare = list(map(int, sys.stdin.readline().strip().split()))

min_charges, max_welfare = 0, max(welfare)
for i in welfare:
    min_charges += max_welfare - i

sys.stdout.write('{}'.format(min_charges))
