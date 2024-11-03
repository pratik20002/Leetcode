class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(nums)): #4 
            if nums[right] == 0: # 0 == 0,  0 == 0, 0 == 0, 0 == 0
                zero_count += 1 # 3
            
            while zero_count > k:  #3 #3
                if nums[left] == 0: #
                    zero_count -= 1 # 2
                
                left += 1 # 2

            max_length = max(max_length, right - left + 1) # 3 - 2 + 1 # 2
        
        return max_length

#T -> O(N)
#S -> O(1)