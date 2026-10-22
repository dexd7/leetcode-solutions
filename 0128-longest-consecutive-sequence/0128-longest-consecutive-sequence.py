class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        temp = set(nums)
        longest_sequence = 0
        for num in temp:
            if num-1 not in temp:
                valid_start = num
                while valid_start in temp:
                    valid_start+=1
                longest_sequence = max(longest_sequence, valid_start-num)
        return longest_sequence
                
