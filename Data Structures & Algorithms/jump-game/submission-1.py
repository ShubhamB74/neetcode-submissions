class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == last:
                return True
            end = min(last, i + nums[i])
            for j in range(i + 1, end + 1):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False          
            return False
        return dfs(0)