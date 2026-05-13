class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackt, stacki = stack.pop()
                res[stacki] = i - stacki
            stack.append((temp, i))
        return res
        