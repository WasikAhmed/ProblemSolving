# Sereja and Dima

import sys

n = int(sys.stdin.readline().strip())
cards = list(map(int, sys.stdin.readline().strip().split()))

l, r = 0, n - 1
sereja, dima = 0, 0

seraja_turn = True
while l <= r:
    if cards[r] > cards[l]:
        if seraja_turn:
            sereja += cards[r]
        else:
            dima += cards[r]
        r -= 1
    else:
        if seraja_turn:
            sereja += cards[l]
        else:
            dima += cards[l]
        l += 1

    seraja_turn = not seraja_turn

# for i in range(n):
#     if i % 2 == 0:
#         if cards[r] >= cards[l]:
#             sereja += cards[r]
#             r -= 1
#         else:
#             sereja += cards[l]
#             l += 1
#     else:
#         if cards[r] >= cards[l]:
#             dima += cards[r]
#             r -= 1
#         else:
#             dima += cards[l]
#             l += 1

sys.stdout.write(f'{sereja} {dima}')
