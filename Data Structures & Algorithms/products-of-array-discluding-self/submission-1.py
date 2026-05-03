class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_count = 1,0
        for n in nums:

            if n:
                product = product* n
            else:
                zero_count += 1
        if zero_count > 1: 
            return [0] * len(nums)
        
        res = [1] * len(nums)
        for i, j in enumerate(nums):
            
            if zero_count:
                res[i] = 0 if j else product
            else:
                res[i] = product // j
        return res