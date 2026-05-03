class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                product = product * nums[j]
            res[i] = product

        return res
        