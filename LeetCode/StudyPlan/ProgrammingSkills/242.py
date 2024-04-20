# Valid Anagram
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))