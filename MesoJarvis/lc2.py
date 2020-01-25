s = "abcabcbb"

def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    map = {}
    max_length = start = 0

    for i in range(len(s)):
        if s[i] in map and start <= map[s[i]]:
            start = map[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        map[s[i]] = i
    return (max_length)

print(lengthOfLongestSubstring(s))