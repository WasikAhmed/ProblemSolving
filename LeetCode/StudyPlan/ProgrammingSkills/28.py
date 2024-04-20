# Find the Index of the First Occurrence in a String
def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


haystack, needle = "sadbutsad", "sad"
print(strStr(haystack, needle))
haystack, needle = "leetcode", "leeto"
print(strStr(haystack, needle))