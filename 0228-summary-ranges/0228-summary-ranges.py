class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        answer = []
        pointer = 0
        while pointer<len(nums):
            start = nums[pointer]
            while pointer+1<len(nums) and nums[pointer]+1 == nums[pointer+1]:
                pointer += 1
            answer.append(str(start) if start == nums[pointer] else f"{start}->{nums[pointer]}" )
            pointer+=1
        return answer
