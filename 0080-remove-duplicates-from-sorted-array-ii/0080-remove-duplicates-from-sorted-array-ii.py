class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        unique_pointer = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[unique_pointer-2]:
                nums[unique_pointer] = nums[i]
                unique_pointer+=1
        return unique_pointer  
