class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common = strs[0]
        pointer = len(common)
        for i in range(1, len(strs)):
            while pointer>0 and common != strs[i][:pointer]:
                pointer-=1
                common = common[:pointer]
                
            if pointer == 0: break
        return common
