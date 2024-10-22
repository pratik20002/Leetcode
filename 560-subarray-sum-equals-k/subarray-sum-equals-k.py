class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res = 0
        # curSum = 0
        # prefixSums = { 0 : 1}
        # for n in nums:
        #     curSum += n
        #     diff =  curSum - k

        #     res += prefixSums.get(diff, 0)
        #     prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        # return res
        # if not nums:
        #     return 0

        # prefix_dict = collections.defaultdict(int)
        # prefix_dict[0] = 1

        # prefix_sum = res = 0

        # for num in nums:
        #     prefix_sum += num

        #     if prefix_sum - k in prefix_dict:
        #         res += prefix_dict[prefix_sum - k]

        #     prefix_dict[prefix_sum] += 1
        
        # return res


        if not nums:
            return 0
        
        prefix_dict = collections.defaultdict(int)
        prefix_dict[0] = 1

        prefix_sum = res = 0
        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_dict:
                res += prefix_dict[prefix_sum - k]
            
            prefix_dict[prefix_sum] += 1
        
        return res