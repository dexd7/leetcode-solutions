class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        duplicate_checker = set()
        pointer = 0
        for num in nums:
            if num in duplicate_checker:
                return True
            duplicate_checker.add(num)
            if len(duplicate_checker)>k:
                duplicate_checker.remove(nums[pointer])
                pointer+=1
        return False
