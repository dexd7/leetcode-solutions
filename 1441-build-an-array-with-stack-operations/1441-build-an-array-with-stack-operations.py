class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        temp = set(target)
        ans = []
        for i in range(1, target[-1]+1):
            if i not in target:
                ans.extend(["Push", "Pop"])
            else:
                ans.append("Push")
        return ans
