class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        #1) Clarify:
        # - Only paranthesis possible is Open brackets no other curly braces or other types.
        # - Total number of pais is 8 at max
        # - order of output doesn't matter
        # - n cannot be 0
        # Example: n = 7
        # total open we can have is 7 since we have total 7 pairs.
        # master string = "((((((()))))))"
        # 
        result = []

        def build(current, opens, closes):
            if len(current) == 2 * n:
                result.append(current)
                return
            if opens<n:                       # rule for adding "("
                build(current + "(", opens + 1, closes)
            if opens>closes:                       # rule for adding ")"
                build(current + ")", opens, closes + 1)

        build("", 0, 0)
        return result
