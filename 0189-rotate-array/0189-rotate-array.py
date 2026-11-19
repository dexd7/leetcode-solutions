class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #each element shifts by k positions, if we imagine our list to be circular, the new index we get is...
        # k transformed to k%len(nums) because if list size is 7 and we expect to rotate 8 positions, then 0 should go to index 1 so (curr_index + k) % len(nums)
        # temp = [0] * len(nums)
        # for ind,num in enumerate(nums):
        #     temp[(ind+k)%len(nums)] = num
        # nums[:] = temp

        #optimized:
        n = len(nums)
        k %= n
        start = count = 0
        while count<n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current+k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if current==start:
                    break
            start+=1
        
