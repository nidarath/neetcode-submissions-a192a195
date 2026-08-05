class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check the strings lengths
    
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}
        # O(n+m) for two hashmaps
        #O(1) space for 52 letter max at most bc 26 diff characters for each 
        
        for letter in s:
            if letter in sMap:
                sMap[letter] += 1
            else: 
                sMap[letter] = 1 

        for letter in t:
            if letter in tMap:
                tMap[letter] += 1
            else:
                tMap[letter] = 1

        for letter, num in sMap.items():
            if letter not in tMap or tMap[letter] != num:               
                return False

        return True