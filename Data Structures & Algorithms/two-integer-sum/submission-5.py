class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            complement = target - n
            if (complement not in seen):
                seen[n] = i
            else:
                return [seen[complement], i]

