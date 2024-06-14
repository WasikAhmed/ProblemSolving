# Beautiful Year

import sys

year = int(sys.stdin.readline().strip())
year += 1

while len(set(str(year))) != len(str(year)):
    year += 1

sys.stdout.write(f'{year}')
