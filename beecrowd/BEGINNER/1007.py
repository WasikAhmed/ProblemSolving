# Difference

import sys

a, b, c, d = map(int, sys.stdin.read().strip().split())
sys.stdout.write(f'DIFERENCA = {(a * b) - (c * d)}\n')
