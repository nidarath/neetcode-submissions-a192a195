class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # convert to hashset
        # set is only keys
        longest = 0 # longest sequence

        for num in numSet:
            if (num - 1) not in numSet: # reset length - check if start
                length = 1
                while (num + length) in numSet:
                    # add to length - check middle
                    length += 1
                longest = max(length, longest) # get largest length
        return longest