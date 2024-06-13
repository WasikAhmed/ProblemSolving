# Marathon

t = int(input())
for i in range(t):
    distinct_integers = [int(i) for i in input().split()]

    print(len([i for i in distinct_integers if i > distinct_integers[0]]))

# Input
# 4
# 2 3 4 1
# 10000 0 1 2
# 500 600 400 300
# 0 9999 10000 9998

# Output
# 2
# 0
# 1
# 3
