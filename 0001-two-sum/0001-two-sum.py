class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        bucket = {}
        for index, num in enumerate(nums):
            required = target-num
            if required in bucket:
                return [bucket[required], index]
            bucket[num] = index
        return []
