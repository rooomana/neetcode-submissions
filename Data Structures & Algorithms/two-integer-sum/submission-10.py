class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for index, number in enumerate(nums):
            remains = target - number
            if (remains in memory):
                return [memory[remains], index]
            memory[number] = index
#        return []
