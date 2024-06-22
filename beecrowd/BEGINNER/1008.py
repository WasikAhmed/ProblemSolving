# Salary

import sys

emp_no, work_hour, amount = map(float, sys.stdin.read().strip().split())
sys.stdout.write(f'NUMBER = {int(emp_no)}\nSALARY = U$ {(work_hour * amount):.2f}\n')
