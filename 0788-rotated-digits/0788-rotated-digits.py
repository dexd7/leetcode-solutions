class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = {0,1,2,5,6,8,9}
        required = {2,5,6,9}
        good_total = 0
        for num in range(1,n+1):
            ok = True
            changed = False
            for digit in str(num):
                digit_int = int(digit)
                if digit_int not in good:
                    ok = False
                    break
                if digit_int in required:
                    changed = True
            if changed and ok:
                good_total+=1
        return good_total
