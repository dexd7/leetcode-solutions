class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # given how much you can jump at max from each position, we have to return true if we can reach the last index else false.
        # first thing that comes to mind is, can there be 0 available total jumps? Do we have to handle negative input as well? although I think that's probably not going to matter. 
        # let's take a few examples here so we can think of an approach:
        # ex 1: nums : [2,3,1,1,4] we know that this one is possible. One thing i already notice is that for it to be impossible, there has to be 0's involved. So my question answered itself.
        # ex 2: nums : [3,2,1,0,4] this one is impossible because second last index is the furthest we can reach from ay point and that is 0, so we can't touch last index.
        # I think it would make sense for us to start from the end instead of the beginning, and if we can reach the start, that means it's possibble to reach the end too.
        # something like:
        #possible = len(nums)-1
        #for i in range(len(nums)-2, -1,-1):
        #   if nums[i]+i>=possible: # meaning if we jump from this index we can reach the current possible end we are at.
        #       possible = i # since we can reach the previous possible end, we update this to be the new possible end.
        # so if we have ex 1 from before:       
        # [2,3,1,1,4]
        possible = len(nums)-1
        for i in range(len(nums)-2, -1,-1):
            if nums[i]+i>=possible:
                possible = i 
        return possible == 0
