### Faster Input and Output Methods in Python

import sys

## Type 1:
## Taking integer as input

# input = sys.stdin.readline().strip()
# n = int(input)
# sys.stdout.write(f'{n}, {type(n)}')
# sys.stdout.flush()

# n = int(sys.stdin.read().strip())
# sys.stdout.write(f'{n}\n')

## Type 2:
## Taking string as input

# s = sys.stdin.readline().strip()
#
# sys.stdout.write(f'{s}, {type(s)}')
# sys.stdout.flush()

# s = sys.stdin.read().strip()
# sys.stdout.write(f'{s}\n')

## Type 3:
## a b c
## 1 2 3

# input = sys.stdin.readline().strip()
# a, b, c = map(int, input.split())
# sys.stdout.write(f'{a}, {b}, {c}')

# a, b, c = map(int, sys.stdin.read().strip().split())
# sys.stdout.write(f'{a} {b} {c}\n')

## Type 4:
## a b c d e...
## 1 2 3 4 5...

# input = sys.stdin.readline().strip()
# arr = list(map(int, input.split()))
# sys.stdout.write(''.join(map(str, arr)) + '\n')
# sys.stdout.write('\n'.join(map(str, arr)) + '\n')

# arr = list(map(int, sys.stdin.read().strip().split()))
# sys.stdout.write(' '.join(map(str, arr)) + '\n')

## Type 5:
## 5
## 1 2 3 4 5

# n = int(sys.stdin.readline().strip())
# arr = list(map(int, sys.stdin.readline().strip().split()))
# sys.stdout.write(f'{n}\n')
# sys.stdout.write(' '.join(map(str, arr)))

# input = sys.stdin.read().strip()
# lines = input.split('\n')
# n = int(lines[0].strip())
# nums = list(map(int, lines[1].strip().split()))
#
# sys.stdout.write(f'{n}\n')
# sys.stdout.write(f' '.join(map(str, nums)) + '\n')

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

# input = sys.stdin.read().strip().split()
# n = int(input[0])
# arr = list(map(int, input[1:n+1]))
# sys.stdout.write(f'{n}\n')
# sys.stdout.write(f' '.join(map(str, arr)) + '\n')

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


# input = sys.stdin.read().strip().split('\n')
# t = int(input[0].strip())
# sys.stdout.write(f'{t}\n')
# index = 1
# for _ in range(t):
#     n = int(input[index].strip())
#     index += 1
#
#     arr = list(map(int, input[index].strip().split()))
#     index += 1
#     # do operations...
#
#     sys.stdout.write(f'{n}\n')
#     sys.stdout.write(f' '.join(map(str, arr)) + '\n')

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

# input = sys.stdin.read().strip().split('\n')
# t = int(input[0].strip())
# sys.stdout.write(f'{t}\n')
#
# index = 1
# for _ in range(t):
#     arr = list(map(int, input[index].strip().split()))
#     index += 1
#     # do operations...
#
#     sys.stdout.write(f' '.join(map(str, arr)) + '\n')
