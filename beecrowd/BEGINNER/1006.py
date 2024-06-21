# Average 2

import sys

A, B, C = map(float, sys.stdin.read().strip().split())

avg = ((A * 2) + (B * 3) + (C * 5)) / (2 + 3 + 5)
sys.stdout.write(f'MEDIA = {avg:.1f}\n')
