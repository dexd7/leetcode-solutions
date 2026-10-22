class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumSquares(n)
            if n == 1:
                return True
        return False
    def sumSquares(self, n):
        res = 0
        while n:
            partial = (n%10)**2
            res+=partial
            n=n//10
        return res
