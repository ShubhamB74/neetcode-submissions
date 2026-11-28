class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        def dfs(i):
            if i == last:
                return True
                
            end = min(last, i + nums[i])
            for j in range(i + 1, end + 1):
                if dfs(j):
                    return True
            return False
        
        return dfs(0)