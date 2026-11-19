class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_pointer = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            nums[unique_pointer] = nums[i]
            unique_pointer+=1
        return unique_pointer
