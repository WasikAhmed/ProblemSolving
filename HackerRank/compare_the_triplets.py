# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    ans = [0, 0]
    for i in range(0, len(a)):
        if(a[i]>b[i]):
            ans[0] = ans[0] + 1
        if(a[i]<b[i]):
            ans[1] = ans[1] + 1
    return ans