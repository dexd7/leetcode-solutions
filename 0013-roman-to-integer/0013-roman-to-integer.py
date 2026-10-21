class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        our_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        integer = 0
        i = 0
        while i < len(s):
            if i+1<len(s) and our_dict[s[i+1]]>our_dict[s[i]]:
                integer += our_dict[s[i+1]]-our_dict[s[i]]
                i+=2
            else:
                integer += our_dict[s[i]]
                i+=1
        return integer
            
