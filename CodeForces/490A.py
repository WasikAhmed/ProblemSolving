# Team Olympiad
import sys

input = sys.stdin.read().strip().split()

n = int(input[0])
skills = list(map(int, input[1:]))

one, two, three = [], [], []

for index, skill in enumerate(skills):
    if skill == 1:
        one.append(index + 1)
    elif skill == 2:
        two.append(index + 1)
    else:
        three.append(index + 1)

min_len = min(len(one), len(two), len(three))
sys.stdout.write(f'{min_len}\n')
for i in range(min_len):
    sys.stdout.write(f'{one[i]} {two[i]} {three[i]}\n')
