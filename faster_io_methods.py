### Faster Input and Output Methods in Python

import sys

## Type 1:
## Taking integer as input

# input = sys.stdin.readline().strip()
# n = int(input)
#
# sys.stdout.write(f'{n}, {type(n)}')
# sys.stdout.flush()

## Type 2:
## Taking string as input

# input = sys.stdin.readline().strip()
# s = input
#
# sys.stdout.write(f'{s}, {type(s)}')
# sys.stdout.flush()

## Type 3:
## a b c
## 1 2 3

# input = sys.stdin.readline().strip()
# a, b, c = map(int, input.split())
#
# sys.stdout.write(f'{a}, {b}, {c}')

## Type 4:
## a b c d e...
## 1 2 3 4 5...

# input = sys.stdin.readline().strip()
# arr = list(map(int, input.split()))
#
# sys.stdout.write(''.join(map(str, arr)) + '\n')
# sys.stdout.write('\n'.join(map(str, arr)) + '\n')

## Type 5:
## 5
## 1 2 3 4 5

# n = int(sys.stdin.readline().strip())
# arr = list(map(int, sys.stdin.readline().strip().split()))
#
# sys.stdout.write(f'{n}\n')
# sys.stdout.write(' '.join(map(str, arr)))

## Type 6:
## 3 -> no. of inputs
## 1
## 2
## 3

# t = int(sys.stdin.readline().strip())
# sys.stdout.write(f'{t}')
# for i in range(t):
#     n = int(sys.stdin.readline().strip())
#     sys.stdout.write(f'{n}')
# do operations...


## Type 7:
## 2
## 3
## 1 2 3
## 5
## 1 2 3 4 5

# t = int(sys.stdin.readline().strip())
# sys.stdout.write(f'{t}')
# for i in range(t):
#     n = int(sys.stdin.readline().strip())
#     sys.stdout.write(f'{n}')
#     arr = list(map(int, sys.stdin.readline().strip().split()))
#     sys.stdout.write(' '.join(map(str, arr)))
# do operations...


## Type 8:
## 4
## 1 2 3 4
## 5 6 7 8
## 9 10 11 12
## 13 14 15 16

# t = int(sys.stdin.readline().strip())
# sys.stdout.write(f'{t}')
# for i in range(t):
#     arr = list(map(int, sys.stdin.readline().strip().split()))
#     sys.stdout.write(' '.join(map(str, arr)))
# do operations...
