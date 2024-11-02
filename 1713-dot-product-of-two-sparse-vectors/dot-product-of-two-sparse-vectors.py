class SparseVector:
    def __init__(self, nums : List[int]):
        self.vector = {i: val for i, val in enumerate(nums) if val != 0}
        
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        for i in self.vector:
            if i in vec.vector:
                dot_product += (self.vector[i] * vec.vector[i])

        return dot_product
        
        
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)