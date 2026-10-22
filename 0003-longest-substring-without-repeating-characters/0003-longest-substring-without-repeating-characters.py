class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = set()
        pointer, max_len = 0, 0
        for ch in s:
            while ch in checker:
                checker.remove(s[pointer])
                pointer+=1
            checker.add(ch)
            max_len = max(max_len, len(checker))
        return max_len
