class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left = 0
        missing = len(t)
        ansl, ansr = 0, float('inf')
        for right, letter in enumerate(s):
            if need[letter]>0:
                missing -= 1
            need[letter] -= 1
            if missing == 0:
                #Shrink window until you hit a letter that had some need. If it ever had some need, it will be 0 at the lowest, and if no need it is negative.
                while need[s[left]]<0:
                    need[s[left]]+=1
                    left+=1
                if (right-left)<(ansr-ansl):
                    ansl, ansr = left, right
                #remove left char to reset validity
                need[s[left]]+=1
                missing+=1
                left+=1


        return s[ansl:ansr+1] if ansr != float('inf') else ""
                
