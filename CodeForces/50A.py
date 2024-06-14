# Domino piling

import sys

M, N = map(int, sys.stdin.readline().strip().split())
sys.stdout.write(f'{(M * N) // 2}')
