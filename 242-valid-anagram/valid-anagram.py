class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tDict = {}
        sDict = {}
        if(len(s) != len(t)):
            return False

        for character in s:
            sDict[character] = sDict.get(character, 0) + 1

        for character in t:
            tDict[character] = tDict.get(character, 0) + 1
        
        return sDict == tDict