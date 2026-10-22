class Solution:
    def isValid(self, s: str) -> bool:
        counters = {')': '(', '}': '{', ']': '['}
        stack = []
        for bracket in s:
            if bracket not in counters:
                stack.append(bracket)
            else:
                if not stack: return False
                last_open_bracket = stack.pop()
                if last_open_bracket != counters[bracket]:
                    return False
        return True if len(stack) == 0 else False
