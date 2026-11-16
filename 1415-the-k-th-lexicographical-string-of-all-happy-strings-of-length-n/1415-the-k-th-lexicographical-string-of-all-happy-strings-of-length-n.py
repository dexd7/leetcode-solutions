class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        #1) Clarify: 1) since n is 10 at the greatest, means we have 10*10^3 possibilities at the maxx which is not that much
        allowed = ['a', 'b', 'c']
        count = 0          # how many happy strings we've finished so far
        answer = ""        # filled in when we hit the k-th one

        def happy(string):
            nonlocal count, answer
            if answer:                      # already found it, stop exploring
                return
            if len(string) == n:
                count += 1
                if count == k:
                    answer = string
                return
            for value in allowed:
                if not string or string[-1] != value:
                    happy(string + value)

        happy("")
        return answer
