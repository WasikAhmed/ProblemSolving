# Merge Strings Alternately

def mergeAlternately(word1: str, word2: str) -> str:
    ptr_1, ptr_2 = 0, 0
    str1_len, str2_len = len(word1), len(word2)
    ans = ""

    while ptr_1 < str1_len and ptr_2 < str2_len:
        ans += word1[ptr_1] + word2[ptr_2]
        ptr_1 += 1
        ptr_2 += 1

    if ptr_1 < str1_len:
        ans += word1[ptr_1:]

    if ptr_2 < str2_len:
        ans += word2[ptr_2:]

    return ans


if __name__ == "__main__":
    # word1, word2 = "abc", "pqr"
    word1, word2 = "abcd", "pq"

    ans = mergeAlternately(word1, word2)
    print(ans)
