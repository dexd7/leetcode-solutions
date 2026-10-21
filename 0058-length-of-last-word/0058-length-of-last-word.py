class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s)
        while s[(index-1)] == ' ':
            index-=1
        wordStart = index
        while wordStart>0 and s[wordStart-1].isalpha():
            wordStart-=1
        return index-wordStart

