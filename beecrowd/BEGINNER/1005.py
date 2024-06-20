# Average 1

import sys

A, B = map(float, sys.stdin.read().strip().split())
avg = ((A * 3.5) + (B * 7.5)) / (3.5 + 7.5)
sys.stdout.write(f'MEDIA = {avg:.5f}\n')
