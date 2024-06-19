# Extremely Basic
import sys

input = sys.stdin.read().strip().split()
sys.stdout.write(f'X = {int(input[0]) + int(input[1])}\n')
