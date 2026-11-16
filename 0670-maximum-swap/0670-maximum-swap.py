class Solution:
    def maximumSwap(self, num: int) -> int:
        #Input: 0 <= num <= 10^8
        # Can be single digit
        # Cannot be negative
        # One swap.
        # num = 2,7,3,6
        # maximum = 0, index = 0
        # 1) maximum = 2, index = 0
        # 2) maximum = 7, index = 1
        # 3) maximum = 7
        # 4) maximum = 7
        # swap indexes 0 and 1, join back the result and give the answer.

        digits = list(str(num))
        best = num
        for i in range(len(digits)):
            for j in range(i+1,len(digits)):
                digits[i], digits[j] = digits[j], digits[i]
                best = max(best, int("".join(digits)))
                digits[i], digits[j] = digits[j], digits[i]
        return best
