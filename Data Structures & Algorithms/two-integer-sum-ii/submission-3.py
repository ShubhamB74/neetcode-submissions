class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = defaultdict(int)

        for i in range(len(numbers)):
            t = target - numbers[i]
            if map[t]:
                return [map[t], i+1]
            map[numbers[i]] = i + 1
        return []        