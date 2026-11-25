class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        # words_set = set(words)

        # def dfs(word):
        #     for i in range(1, len(word)):
        #         prefix = word[:i]
        #         suffix = word[i:]
        #         if (prefix in words_set and suffix in words_set) or (prefix in words_set and dfs(suffix)):
        #             return True 
        # res = []
        # for i in range(len(words)):
        #     if dfs(words[i]):
        #         res.append(words[i])
        # return res
        # O(N*l^4) N = len words, l = length of word

        words_set = set(words)
        dp = {}
        def dfs(word):
            if word in dp:
                return dp[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if (prefix in words_set and suffix in words_set) or (prefix in words_set and dfs(suffix)):
                    dp[word] = True
                    return dp[word]
            dp[word] = False
            return dp[word] 
        res = []
        for i in range(len(words)):
            if dfs(words[i]):
                res.append(words[i])
        return res
