class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #check for differing lengths
            return False

        sMap, tMap = {}, {}

        #.get(letter, 0) where 0 is what is returned when the value doesn exist
        # letter is searched for its value
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        return sMap == tMap # compare the two maps bc if same its an anagram