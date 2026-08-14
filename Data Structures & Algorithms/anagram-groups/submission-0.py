class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #hashmap: key-value pair where the value is a list
        for s in strs:
            count = [0] * 26 # make a array of 0s with 26 spots
            for c in s:
                count[ord(c) - ord('a')] += 1 # increment the index of the char
            res[tuple(count)].append(s) # add it as a tuple as key, append real word as value
        return list(res.values()) # return the list of the hashmap

#ord(c) - ord('a'), gets the numerical ASCII value of a character. maps the letters to a 0-25 index