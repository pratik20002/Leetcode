class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
   
    #1
    def pickIndex(self):
        target = random.randint(1, self.prefix_sums[-1])
        l, r = 0, len(self.prefix_sums) - 1

        while l < r:
            mid = (l + r)//2
            if self.prefix_sums[mid] < target:
                l = mid + 1
            else:
                r = mid
            
        return l
        