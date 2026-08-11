class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, n in enumerate(nums):
            res = target - n
            if (res in mem and mem[res] != i):
                return [mem[res], i]
            mem[n] = i