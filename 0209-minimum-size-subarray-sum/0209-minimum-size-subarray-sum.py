class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = float('inf')
        pointer, total = 0, 0
        for i in range(len(nums)):
            total+=nums[i]
            while total>=target:
                min_len = min(min_len, i-pointer+1)
                total-=nums[pointer]
                pointer+=1
        return min_len if min_len != float('inf') else 0
