class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        #1) Clarify: 1) since n is 10 at the greatest, means we have 10*10^3 possibilities at the maxx which is not that much
        happy_strings = []
        allowed = ['a', 'b', 'c']
        def happy(string):
            if len(string) == n:
                happy_strings.append(string)
                return
            for value in allowed:
                if not string or string[-1] != value:
                    happy(string+value)
        happy("")
        return happy_strings[k-1] if k-1<len(happy_strings) else ""
