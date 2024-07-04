# Simple Calculate

import sys

input = sys.stdin.read().strip().split()

prod1_unit, prod2_unit = int(input[1]), int(input[4])
prod1_price, prod2_price = float(input[2]), float(input[5])

sys.stdout.write(f'VALOR A PAGAR: R$ {((prod1_unit * prod1_price) + (prod2_unit * prod2_price)):.2f}\n')
