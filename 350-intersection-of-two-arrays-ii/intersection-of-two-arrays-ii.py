class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        freq = {}

        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        return result

        