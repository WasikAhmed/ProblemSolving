# Salary with Bonus

import sys

input = sys.stdin.read().strip().split()
sys.stdout.write(f'TOTAL = R$ {float(input[1]) + (float(input[2]) * 0.15):.2f}\n')
