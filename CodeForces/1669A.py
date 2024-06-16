# Division?

import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    rating = int(sys.stdin.readline().strip())

    if rating <= 1399:
        sys.stdout.write('Division 4\n')
    elif 1400 <= rating <= 1599:
        sys.stdout.write('Division 3\n')
    elif 1600 <= rating <= 1899:
        sys.stdout.write('Division 2\n')
    else:
        sys.stdout.write('Division 1\n')
