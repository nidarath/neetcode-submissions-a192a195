class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    #sorting solution
        res = 0 # output
        if not nums: # if nums is empty return 0
            return 0    
        nums.sort() # sort the array

        curr, streak, i = nums[0], 0, 0 
        while i < len(nums):
            if curr != nums[i]: #if nums[i] doesnt match curr 
                curr = nums[i] # reset curr and streak
                streak = 0 
            while i < len(nums) and nums[i] == curr: # O(n) advances i
                i += 1 # skips duplicates
            streak += 1 # add to streak and curr to count
            curr += 1
            res = max(res,streak) # choose max 
        #O(nlogn) where while loop is (n + n) cuz advancing and sorting is nlogn
        return res