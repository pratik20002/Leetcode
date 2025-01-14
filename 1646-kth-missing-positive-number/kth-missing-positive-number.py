class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        # #CASE 1 - IF ARRAY DOES NOT START AT 1 
        # if arr[0] != 1:
        #     if arr[0] - 1 >= k:
        #         return k
        #     else:
        #         k -= arr[0] - 1
        
        # i = 0
        # #CASE 2 - IF THE K LIES IN BETWEEN
        # while i < len(arr) - 1:
        #     diff = arr[i + 1] - arr[i]
        #     if diff != 1:
        #         for num in range(arr[i] + 1, arr[i + 1]):
        #             k -= 1

        #             if not k:
        #                 return num
            
        #     i += 1
        
        # #CASE 3 - IF K IS BEYOND THE ARR
        # if k:
        #     return arr[-1] + k

        left , right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right)// 2
            missing_count = arr[mid] - (mid + 1)

            if missing_count < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return k + left


# T -> O(N)
# S -> O(1)