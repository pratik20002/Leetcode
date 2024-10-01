class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        current_number = 1
        idx = 0
        n = len(arr)
        while missing_count < k:
            if idx >= n or arr[idx] != current_number:
                missing_count += 1

                if missing_count == k:
                    return current_number
            
            else:
                idx += 1
            
            current_number += 1