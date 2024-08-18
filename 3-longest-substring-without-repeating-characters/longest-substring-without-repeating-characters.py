class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
    
        start = 0
        max_length = 0
        
        for i, char in enumerate(s):
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            last_seen[char] = i
            max_length = max(max_length, i - start + 1)
        
        return max_length