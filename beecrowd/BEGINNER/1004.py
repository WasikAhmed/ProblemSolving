# Simple Product

import sys

input = sys.stdin.read().strip().split()
sys.stdout.write(f'PROD = {int(input[0]) * int(input[1])}\n')
