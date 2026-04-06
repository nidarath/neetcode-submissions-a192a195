class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hash map to store the index and character
        # key value pair: key = s[r] and value = index r
        mp = {}
        # initialize our left pointer
        l= 0
        # our result variable
        res = 0
        # where r is right pointer
        for r in range(len(s)):
            # if val @ right pointer is in mp:
            if s[r] in mp:
                # move left ptr to 
                # max(arg1,arg2): chooses larger one
                l = max(mp[s[r]] + 1, l)
            # update hash map each time with last index of each character
            mp[s[r]] = r
            # result will be equal to the largest window size
            # compare current res with new window each time
            res = max(res, r - l + 1)
        # return the ending result
        return res 
