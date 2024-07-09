# Mishka and Game

import sys

input = list(map(int, sys.stdin.read().strip().split()))

n = input[0]

mishka, chris = 0, 0
for i in range(1, n * 2, 2):
    if input[i] > input[i + 1]:
        mishka += 1
    if input[i] < input[i + 1]:
        chris += 1

if mishka > chris:
    sys.stdout.write('Mishka\n')
elif mishka < chris:
    sys.stdout.write('Chris\n')
else:
    sys.stdout.write('Friendship is magic!^^\n')
