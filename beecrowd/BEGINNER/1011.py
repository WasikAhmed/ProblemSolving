# Sphere

import sys
pi = 3.14159

R = float(sys.stdin.read().strip())
vol = (4/3) * pi * (R ** 3)

sys.stdout.write(f'VOLUME = {vol:.3f}\n')

