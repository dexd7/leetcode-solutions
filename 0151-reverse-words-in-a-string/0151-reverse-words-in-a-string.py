class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        pointer = len(s)
        ans = []
        while pointer>0:
            while s[pointer-1] == ' ' and pointer>0:
                pointer-=1
            word_end = pointer
            while s[pointer-1] != ' ' and pointer>0:
                pointer-=1
            ans.append(s[pointer:word_end])
        return ' '.join(ans)
                
